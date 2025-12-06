from fastapi import FastAPI
import mlflow.xgboost
import pandas as pd
import uvicorn
import os

app = FastAPI(title="Netflix-Like Recommender API")

# Load model from local MLflow run (Simulating Production Registry)
# In real MLOps, you fetch from S3/Model Registry. 
# Here we grab the latest run from the 'mlruns' folder for simplicity.
def get_latest_model_path():
    # Helper to find where MLflow saved the last model
    return "runs:/" + mlflow.search_runs(experiment_names=["Netflix_RecSys_v1"]).iloc[0].run_id + "/recommender_model"

@app.on_event("startup")
def load_model():
    global model
    try:
        model_uri = get_latest_model_path()
        model = mlflow.xgboost.load_model(model_uri)
        print("✅ Model loaded successfully.")
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        model = None

@app.post("/predict")
def predict(user_id: int, movie_id: int, genre_code: int):
    """
    Predicts the rating a user will give to a movie.
    """
    if not model:
        return {"error": "Model not loaded. Train the model first."}
    
    input_data = pd.DataFrame([[user_id, movie_id, genre_code]], 
                              columns=['userId', 'movieId', 'genre_code'])
    
    prediction = model.predict(input_data)
    return {
        "user_id": user_id,
        "movie_id": movie_id,
        "predicted_rating": float(prediction[0]),
        "recommendation": "Recommended" if prediction[0] > 3.5 else "Not Recommended"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)