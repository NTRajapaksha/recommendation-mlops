// ⚠️ REPLACE THIS with your actual Public API URL from the 'PORTS' tab
const API_BASE = "https://laughing-space-disco-rj56vqgqpj7c5gjw-8000.app.github.dev"; 

async function predict() {
    // 1. Get Inputs
    const userId = document.getElementById('userId').value;
    const movieSelect = document.getElementById('movieSelect');
    const movieId = movieSelect.value;
    const genreCode = movieSelect.options[movieSelect.selectedIndex].getAttribute('data-genre');
    
    // 2. Prepare UI
    const btn = document.querySelector('.analyze-btn');
    const card = document.getElementById('resultCard');
    
    btn.innerText = "Running Model...";
    btn.disabled = true;
    card.classList.add('hidden'); // Hide old results

    // 3. Call API
    // We force HTTPS to avoid "Mixed Content" errors
    const url = `${API_BASE}/predict?user_id=${userId}&movie_id=${movieId}&genre_code=${genreCode}`;

    try {
        const response = await fetch(url, { method: 'POST' });
        const data = await response.json();
        
        // --- RENDER RESULTS (Using your JSON format) ---
        
        // Update Text
        document.getElementById('ratingValue').innerText = data.predicted_rating.toFixed(2);
        document.getElementById('movieIdDisplay').innerText = data.movie_id;
        document.getElementById('userIdDisplay').innerText = data.user_id;

        const statusEl = document.getElementById('recStatus');
        
        if (data.recommendation === "Recommended") {
            statusEl.innerText = "✅ RECOMMENDED";
            statusEl.style.backgroundColor = "#46d369"; // Green
            statusEl.style.color = "black";
        } else {
            statusEl.innerText = "❌ NOT RECOMMENDED";
            statusEl.style.backgroundColor = "#e50914"; // Netflix Red
            statusEl.style.color = "white";
        }
        
        // Show Card
        card.classList.remove('hidden');

    } catch (error) {
        alert("Error connecting to API. Check console for details.");
        console.error(error);
    } finally {
        btn.innerText = "Run Prediction";
        btn.disabled = false;
    }
}