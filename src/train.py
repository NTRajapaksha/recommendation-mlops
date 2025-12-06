import pandas as pd
import xgboost as xgb
import shap
import mlflow
import mlflow.xgboost
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
import os
import requests
import zipfile
import io

# --- 1. Data Ingestion (Automation) ---
def load_data():
    print("📥 Downloading MovieLens Dataset...")
    url = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall("data")
    
    # Load Ratings and Movies
    ratings = pd.read_csv("data/ml-latest-small/ratings.csv")
    movies = pd.read_csv("data/ml-latest-small/movies.csv")
    
    # Merge to create a rich dataset
    data = pd.merge(ratings, movies, on='movieId')
    
    # Simple Feature Engineering: Convert Genres to Category Codes
    data['genre_code'] = data['genres'].astype('category').cat.codes
    return data

# --- 2. Training & MLOps ---
def train():
    mlflow.set_experiment("Netflix_RecSys_v1")
    
    data = load_data()
    
    # Features: UserID, MovieID, Genre (In real prod, use more user demographics)
    X = data[['userId', 'movieId', 'genre_code']]
    y = data['rating']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    with mlflow.start_run():
        print("🚀 Training XGBoost Model...")
        
        # XGBoost Params for 4-Core efficiency
        params = {
            "n_estimators": 100,
            "learning_rate": 0.1,
            "max_depth": 5,
            "n_jobs": 4  # Utilize all Codespace cores
        }
        
        model = xgb.XGBRegressor(**params)
        model.fit(X_train, y_train)
        
        # Predictions
        predictions = model.predict(X_test)
        
        # Metrics
        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        mae = mean_absolute_error(y_test, predictions)
        
        print(f"✅ Model Performance - RMSE: {rmse:.4f}, MAE: {mae:.4f}")
        
        # Log to MLflow
        mlflow.log_params(params)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        
        # Log Model
        mlflow.xgboost.log_model(model, "recommender_model")
        
        # --- 3. Explainability (SHAP) ---
        print("🔍 Generating Explanations...")
        explainer = shap.Explainer(model)
        shap_values = explainer(X_test.iloc[:100]) # Explain first 100 predictions
        
        # Save a summary plot
        shap.plots.beeswarm(shap_values, show=False)
        import matplotlib.pyplot as plt
        plt.savefig("shap_summary.png")
        mlflow.log_artifact("shap_summary.png")
        print("📊 SHAP Summary saved to MLflow artifacts.")

if __name__ == "__main__":
    train()