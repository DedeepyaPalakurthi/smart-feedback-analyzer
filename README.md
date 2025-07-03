# 💬 Smart Feedback Analyzer

An API-powered sentiment analysis engine built with **FastAPI**, designed to analyze user feedback in real-time. Ideal for customer support tools, review dashboards, or internal product monitoring systems.

---

## 🚀 Features

- 🔍 Predicts sentiment (Positive, Neutral, Negative) from raw text input
- ⚡ Built using FastAPI for high performance and simplicity
- 🧠 Includes a plug-and-play ML model (Scikit-learn or Transformers ready)
- 🧪 Unit-tested with `pytest`
- 📦 Containerized using Docker
- 🔁 Ready for CI/CD pipeline integration

---

## 🛠️ Tech Stack

- **Language**: Python 3.12  
- **API**: FastAPI  
- **ML**: Scikit-learn (can swap with HuggingFace transformers)  
- **Testing**: Pytest  
- **Containerization**: Docker  
- **Deployment-ready**: CI/CD setup support (GitHub Actions)

---

## 📂 Project Structure

```
smart-feedback-analyzer/
├── app/
│   ├── main.py            # FastAPI routes
│   ├── model.py           # Sentiment logic
│   └── schemas.py         # Pydantic models
├── tests/                 # Unit tests
├── Dockerfile             # For containerized deployment
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## 🧪 Run Locally

### 1. Clone the Repo
```bash
git clone git@github.com:DedeepyaPalakurthi/smart-feedback-analyzer.git
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

### 4. Start the API Server
```bash
uvicorn app.main:app --reload
```

Open your browser at:  
👉 `http://127.0.0.1:8000/docs` to test the Swagger UI

---

## 🧪 Run Tests
```bash
pytest
```

---

## 🐳 Docker (Optional)
```bash
docker build -t feedback-analyzer .
docker run -p 8000:8000 feedback-analyzer
```

---

## ✍️ Example Request

**POST** `/predict`
```json
{
  "text": "This product is amazing and easy to use!"
}
```

**Response**
```json
{
  "sentiment": "Positive"
}
```

---

## 📌 Future Enhancements

- Add support for multilingual sentiment analysis
- Integrate MongoDB/PostgreSQL for feedback storage
- Deploy to AWS/GCP with CI/CD
- Add real-time dashboard using Streamlit

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

## 📄 License

MIT License. Free to use and modify.
