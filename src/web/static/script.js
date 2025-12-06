async function getPrediction(userId, movieId, genreCode, element) {
    const url = `http://localhost:8000/predict?user_id=${userId}&movie_id=${movieId}&genre_code=${genreCode}`;
    
    try {
        const response = await fetch(url, { method: 'POST' });
        const data = await response.json();
        
        const score = Math.round((data.predicted_rating / 5) * 100);
        let color = score > 80 ? '#46d369' : (score > 50 ? 'orange' : 'red');
        
        element.innerHTML = `<span style="color:${color}">${score}% Match</span>`;
    } catch (error) {
        console.error("API Error:", error);
        element.innerHTML = "<span style='color:grey'>N/A</span>";
    }
}

function refreshPredictions() {
    const userId = document.getElementById('userIdInput').value;
    const cards = document.querySelectorAll('.movie-card');

    cards.forEach(card => {
        const movieId = card.getAttribute('data-movie-id');
        const genreCode = card.getAttribute('data-genre-code');
        const scoreElement = card.querySelector('.match-score');
        
        // Show loading state
        scoreElement.innerText = "...";
        
        // Call API
        getPrediction(userId, movieId, genreCode, scoreElement);
    });
}

// Run on initial load
document.addEventListener('DOMContentLoaded', refreshPredictions);