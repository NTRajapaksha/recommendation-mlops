from flask import Flask, render_template
import pandas as pd
import random

app = Flask(__name__)

# Load data once when app starts
def get_random_movies():
    # In a real app, this comes from a database. Here we use the CSV.
    try:
        movies = pd.read_csv("data/ml-latest-small/movies.csv")
        movies['genre_code'] = movies['genres'].astype('category').cat.codes
        # Pick 12 random movies to display
        return movies.sample(12).to_dict(orient='records')
    except:
        return []

@app.route('/')
def home():
    movies = get_random_movies()
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)