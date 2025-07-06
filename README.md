# 💬 Smart Feedback Analyzer

A production-ready, API-driven sentiment analysis engine built using **FastAPI** and deployed with **CI/CD pipelines** on **Google Cloud Run**. Designed for scalable real-time analysis of customer feedback, reviews, or internal product insights.

---

## 🚀 Key Features

- 🔍 **Real-Time Sentiment Analysis** — Predicts Positive, Neutral, or Negative sentiment
- ⚡ **High-Performance API** — Built with FastAPI, optimized for async requests
- 🐳 **Dockerized & Cloud Native** — Fully containerized with Docker, deployed via Cloud Run
- 🔁 **CI/CD Ready** — GitHub Actions pipeline auto-builds, tests, and deploys
- 🧪 **Robust Testing** — Unit-tested with Pytest for reliability and maintainability

---

## 🛠 Tech Stack

| Layer              | Tools & Frameworks                            |
|-------------------|------------------------------------------------|
| **Language**       | Python 3.10                                    |
| **API Framework**  | FastAPI                                        |
| **ML Model**       | Scikit-learn (Transformers-ready)              |
| **Testing**        | Pytest                                         |
| **Containerization**| Docker                                        |
| **CI/CD**          | GitHub Actions + Google Cloud Build & Run     |
| **Cloud Platform** | Google Cloud Platform (Artifact Registry, Cloud Run) |

---

## 📁 Project Structure

```
smart-feedback-analyzer/
├── app/
│   ├── main.py # FastAPI entry point
│   ├── model.py # Sentiment classification logic
│   └── schemas.py # Pydantic request/response schemas
├── tests/ # Pytest unit tests
├── Dockerfile # Docker image definition
├── .github/workflows/ # GitHub Actions CI/CD pipeline
├── requirements.txt # Python dependencies
└── README.md # You're here!
```

---

## 🧪 Run Locally

### 1. Clone & Set Up
```bash
git clone https://github.com/DedeepyaPalakurthi/smart-feedback-analyzer.git
cd smart-feedback-analyzer
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the API
```bash
uvicorn app.main:app --reload
```
📍 Visit http://127.0.0.1:8000/docs to test in Swagger UI.

---

## 🧪 Run Tests
```bash
pytest
```

---

## 🐳 Docker Usage
```bash
docker build -t feedback-analyzer .
docker run -p 8000:8000 feedback-analyzer
```

---

## ☁️ CI/CD & Deployment

This project is configured to auto-deploy on push to main using:

- GitHub Actions
- GCP Artifact Registry
- Cloud Run

To redeploy manually:

```bash
gcloud run deploy smart-feedback-api   --image us-central1-docker.pkg.dev/PROJECT_ID/REPO/feedback-analyzer   --platform managed   --region us-central1   --allow-unauthenticated
```

---

## 📦 Example API Request

### POST `/predict`
```json
{
  "text": "The customer service was excellent!"
}
```

### Response:
```json
{
  "sentiment": "Positive"
}
```

---

## 📌 Future Improvements

- [ ] Streamlit dashboard for real-time feedback analysis
- [ ] Multilingual sentiment classification
- [ ] Integration with MongoDB/PostgreSQL
- [ ] Logging & monitoring setup (Stackdriver or Prometheus)

---

## 👩‍💻 Maintainer

**Dedeepya Palakurthi**  
Graduate, MS in Data Science – UMBC  
Open to Data Engineer / ML Infra / AI Platform roles  
📫 Connect: [LinkedIn](https://www.linkedin.com/in/dedeepya-palakurthi-366653204/)
