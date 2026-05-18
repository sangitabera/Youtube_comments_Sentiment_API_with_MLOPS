# 🎥 YouTube Comment Sentiment Analysis System

A production-ready NLP-based sentiment analysis system for YouTube comments built using Machine Learning, FastAPI, Streamlit, Explainable AI, Docker, and modern MLOps concepts.


# 🚀 Project Overview

This project predicts the sentiment of YouTube comments as:

- ✅ Positive
- ❌ Negative
- ⚪ Neutral

The system includes:

- End-to-end ML pipeline
- NLP preprocessing
- TF-IDF feature extraction
- Explainable AI (LIME)
- FastAPI backend
- Streamlit frontend
- Docker containerization
- Logging
- Rate limiting
- API deployment architecture


# 🧠 Machine Learning Workflow

## Data Processing
- Text cleaning
- Lowercasing
- Stopword removal
- Tokenization
- Feature extraction using TF-IDF

## Model Training
- Train-test split
- Cross-validation
- Hyperparameter tuning
- Pipeline-based training
- Model serialization using Joblib

## Algorithms Used
- Multinomial Naive Bayes
- Logistic Regression


# 🔍 Explainable AI

The project uses:

## LIME (Local Interpretable Model-Agnostic Explanations)

LIME explains:
- Why a prediction happened
- Which words influenced the prediction
- Importance score of each feature

Example:

| Word | Importance |
|------|------------|
| amazing | +0.52 |
| worst | -0.67 |



# 🏗️ System Architecture

```text
Streamlit Frontend
        ↓
FastAPI Backend
        ↓
ML Pipeline (.pkl)
        ↓
LIME Explainability
```

---

# ⚡ Features

- ✅ Real-time sentiment prediction
- ✅ Explainable predictions
- ✅ REST API with FastAPI
- ✅ Streamlit interactive UI
- ✅ API rate limiting
- ✅ Logging system
- ✅ Dockerized deployment
- ✅ Production-ready architecture



# 📂 Project Structure

```text
Youtube_comment_sentiment_Analysis/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   │
│   ├── model/
│   │   └── sentiment_pipeline.pkl
│   │
│   ├── logs/
│   │   └── app.log
│   │
│   └── utils/
│       └── logger.py
│
├── frontend/
│   ├── streamlit_app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
├── README.md
└── .gitignore
```



# 🛠️ Tech Stack

## Machine Learning
- Scikit-learn
- Pandas
- NumPy

## NLP
- TF-IDF Vectorization
- Text preprocessing

## Explainability
- LIME

## Backend
- FastAPI
- Uvicorn

## Frontend
- Streamlit

## Deployment & DevOps
- Docker
- Docker Compose



# 📊 API Endpoints

## Predict Sentiment

```http
POST /predict
```

### Request

```json
{
  "comment": "This video is amazing"
}
```

### Response

```json
{
  "comment": "This video is amazing",
  "sentiment": "Positive"
}
```

---

## Explain Prediction

```http
POST /explain
```

### Response

```json
{
  "prediction": "Positive",
  "explanation": [
    ["amazing", 0.52],
    ["video", 0.11]
  ]
}
```


# 🚀 Running Locally

## 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd Youtube_comment_sentiment_Analysis
```



## 2️⃣ Create Virtual Environment

```bash
python -m venv myenv
```

### Activate Environment

#### Windows
```bash
myenv\Scripts\activate
```

#### Linux/Mac
```bash
source myenv/bin/activate
```



## 3️⃣ Install Dependencies

### Backend

```bash
cd backend
pip install -r requirements.txt
```

### Frontend

```bash
cd ../frontend
pip install -r requirements.txt
```



# ▶️ Run Application

## Start FastAPI Backend

```bash
cd backend
uvicorn app:app --reload
```

Backend:
```text
http://127.0.0.1:8000
```

Swagger Docs:
```text
http://127.0.0.1:8000/docs
```



## Start Streamlit Frontend

```bash
cd frontend
streamlit run streamlit_app.py
```

Frontend:
```text
http://localhost:8501
```



# 🐳 Docker Setup

## Build and Run Containers

```bash
docker-compose up --build
```



# 📈 Future Improvements

- JWT Authentication
- Redis caching
- PostgreSQL integration
- MLflow experiment tracking
- Kubernetes deployment
- Cloud deployment (AWS/GCP/Azure)
- CI/CD automation
- Monitoring dashboards



# 📌 Key Learning Outcomes

This project demonstrates:

- End-to-end ML workflow
- NLP pipeline creation
- Explainable AI integration
- REST API development
- Frontend-backend integration
- Docker containerization
- Production-level project structuring
- MLOps fundamentals


# 👩‍💻 Author

## Sangita Bera

Machine Learning | NLP | FastAPI | Streamlit | MLOps Enthusiast


# ⭐ If you found this project useful, consider giving it a star.
