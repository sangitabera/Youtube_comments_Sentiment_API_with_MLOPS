# YouTube Comment Sentiment Analysis System

A production-level Machine Learning application that performs sentiment analysis on YouTube comments using FastAPI, Streamlit, Docker, Redis, Explainable AI, and automated testing.



## Features

- Sentiment Prediction
- Positive / Negative / Neutral Classification
- FastAPI REST API
- Streamlit Frontend
- Explainable AI Support
- Redis Rate Limiting
- Dockerized Application
- Automated API Testing with Pytest
- Logging System
- CI/CD Ready Structure
- Scalable Project Architecture



# Tech Stack

## Machine Learning
- Scikit-learn
- TF-IDF Vectorizer
- Multinomial Naive Bayes

## Backend
- FastAPI
- Uvicorn
- Redis
- SlowAPI

## Frontend
- Streamlit

## DevOps
- Docker
- Docker Compose
- GitHub Actions

## Testing
- Pytest
- FastAPI TestClient


# Project Structure

```text
Youtube_comment_sentiment_Analysis/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── backend/
│   │
│   ├── model/
│   │   ├── sentiment_model.pkl
│   │   └── label_encoder.pkl
│   │
│   ├── logs/
│   │   └── app.log
│   │
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_api.py
│   │   ├── test_input.py
│   │   └── test_rate_limiting.py
│   │
│   ├── __init__.py
│   ├── app.py
│   ├── logger.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── streamlit_app.py
│   ├── Dockerfile
│   └── requirements2.txt
│
├── data/
│   └── YoutubeCommentsDataset.csv
│
├── notebook/
│   └── youtube-comments-sentiment.ipynb
│
├── .gitignore
├── docker-compose.yml
├── README.md
```



# Model Pipeline

1. Text Cleaning
2. TF-IDF Vectorization
3. Model Training
4. Sentiment Prediction
5. Explainable AI Visualization



# Sentiment Labels

| Label | Sentiment |
|------|------|
| 0 | Negative |
| 1 | Positive |
| 2 | Neutral |



# Installation

## Clone Repository

```bash
git clone <repository_url>
cd Youtube_comment_sentiment_Analysis
```

---

# Create Virtual Environment

```bash
python -m venv myenv
```

Activate environment:

## Windows

```bash
myenv\Scripts\activate
```

## Linux/Mac

```bash
source myenv/bin/activate
```

---

# Install Dependencies

## Backend

```bash
pip install -r backend/requirements.txt
```

## Frontend

```bash
pip install -r frontend/requirements2.txt
```



# Run FastAPI Backend

```bash
uvicorn backend.app:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```



# Run Streamlit Frontend

```bash
streamlit run frontend/streamlit_app.py
```

Frontend runs on:

```text
http://localhost:8501
```



# API Endpoint

## Predict Sentiment

### POST `/predict`

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

# Explainable AI Endpoint

## POST `/explain`

Provides prediction explanation for user comments.

---

# Redis Setup

Run Redis using Docker:

```bash
docker run -d --name redis-container -p 6379:6379 redis
```

Verify container:

```bash
docker ps
```

---

# Docker Setup

## Build Backend

```bash
docker build -t sentiment-backend ./backend
```

## Build Frontend

```bash
docker build -t sentiment-frontend ./frontend
```

---

# Docker Compose

Run complete application:

```bash
docker-compose up --build
```

---

# Run Tests

```bash
pytest -v
```

Expected Result:

```text
================ 4 passed =================
```

---

# Rate Limiting

API uses Redis-based rate limiting.

Example:

```python
@limiter.limit("5/minute")
```

---

# Logging

Application logs are stored in:

```text
backend/logs/app.log
```

---

# CI/CD

GitHub Actions workflow included for:

- Automated Testing
- Build Validation
- Deployment Ready Setup

Workflow File:

```text
.github/workflows/ci.yml
```

---

# Future Improvements

- Transformer-based Models
- HuggingFace Integration
- Kubernetes Deployment
- Monitoring with Prometheus
- Grafana Dashboard
- JWT Authentication
- Cloud Deployment



# Author

Sangita Bera



# License

This project is licensed under the MIT License.