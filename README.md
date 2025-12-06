# 🎬Recommendation System (MLOps & Full Stack)

![Python](https://img.shields.io/badge/Python-3.9-blue)
![MLOps](https://img.shields.io/badge/MLOps-Pipeline-green)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-teal)
![Flask](https://img.shields.io/badge/Frontend-Flask-orange)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-red)

A scalable, end-to-end Machine Learning recommendation engine built with MLOps best practices. It mimics a streaming platform's "Match Score" feature, using **XGBoost** for ranking and **SHAP** for model explainability.

## 🏗️ Architecture

The project follows a decoupled **Microservices Architecture**:

1. **The Brain (Model API):** A **FastAPI** service serving an XGBoost Regressor. It handles inference and returns predicted ratings + explainability metrics.
2. **The Face (Frontend):** A **Flask** web application providing a "Netflix-like" dashboard for users to browse movies and check compatibility.
3. **The Spine (MLOps):**
   * **MLflow:** For experiment tracking and model versioning.
   * **GitHub Actions:** For CI/CD (automated testing on push).
   * **Makefile:** For build automation.

---

## 🚀 Features

* **Real-time Inference:** Sub-millisecond latency for predicting user-movie compatibility.
* **Explainable AI (XAI):** Integrated **SHAP (SHapley Additive exPlanations)** to understand *why* a movie is recommended.
* **Automated Pipeline:** Data ingestion, processing, and training are automated via script.
* **CI/CD Integration:** GitHub Actions workflow ensures code quality and model artifact generation on every commit.
* **Interactive Dashboard:** A sleek, dark-mode UI to simulate the user experience.

---

## 🛠️ Tech Stack

* **Language:** Python 3.9
* **Machine Learning:** XGBoost, Scikit-Learn, Pandas
* **MLOps:** MLflow, Pytest, GitHub Actions
* **Backend:** FastAPI, Uvicorn
* **Frontend:** Flask, HTML5, CSS3, JavaScript (Fetch API)
* **Data:** MovieLens Small Dataset

---

## 💻 Getting Started

### 1. Prerequisites
This project is optimized for **GitHub Codespaces** (4-core environment) but runs on any standard Linux/Mac environment.

### 2. Installation
Use the `Makefile` to set up the environment automatically:

```bash
make install
```

### 3. Train the Model
This command downloads the MovieLens data, processes features, trains the XGBoost model, and logs metrics/artifacts to MLflow.

```bash
make train
```

Artifacts generated: `models/`, `mlruns/`, `shap_summary.png`

### 4. Run the Application
Launch both the FastAPI Backend and Flask Frontend simultaneously:

```bash
make run-full-stack
```

* **Frontend (UI):** Open http://localhost:5000
* **Backend (API):** Running on http://localhost:8000

⚠️ **Note for Codespaces Users:** Ensure both Port 5000 and 8000 are set to Public Visibility in the "Ports" tab.

---

## 🧪 MLOps Automation

### Continuous Integration (CI)
A GitHub Actions workflow (`.github/workflows/mlops.yml`) runs on every push to `main`. It performs:

* **Environment Setup:** Installs dependencies.
* **Smoke Testing:** Runs pytest to ensure the training pipeline executes without errors and generates valid artifacts.

To run tests locally:

```bash
export PYTHONPATH=$PYTHONPATH:.
pytest tests/test_pipeline.py
```

---

## 📂 Project Structure

```
├── .github/workflows/   # CI/CD Pipeline configuration
├── data/                # Raw and processed data (Git-ignored)
├── mlruns/              # MLflow experiment logs
├── src/
│   ├── api/             # FastAPI backend code
│   ├── web/             # Flask frontend (templates/static)
│   └── train.py         # Training pipeline script
├── tests/               # Unit and integration tests
├── Makefile             # Automation commands
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🔮 Future Improvements

- [ ] Add Docker containerization for easier deployment.
- [ ] Integrate Redis for caching frequent predictions.
- [ ] Add "User Age" and demographic data for richer recommendations.
- [ ] Deploy to AWS Lambda or Google Cloud Run.
