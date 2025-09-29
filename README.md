

# 🧠 Generative AI Virtual Assistant

A modular, containerized **virtual assistant** built with **FastAPI**, **LangChain**, and **Docker**.  
This project demonstrates how to integrate **Large Language Models (LLMs)** into a production-ready backend service.

---

## 📌 Features

- 🚀 **FastAPI backend** – high-performance async API for inference and orchestration  
- 🔗 **LangChain integration** – modular chains, tools, and memory support  
- 🐳 **Dockerized deployment** – ready to containerize and scale with `docker-compose`  
- 🗄️ **Config-driven architecture** – easily swap models, embeddings, or vector DBs  
- 🧩 **Extensible design** – add tools (retrieval, APIs, databases) seamlessly  

---

## 📂 Repository Structure

```

generative-ai-assistant/
├── app/
│   ├── **init**.py
│   ├── main.py               # FastAPI entrypoint
│   ├── api/
│   │   ├── **init**.py
│   │   └── v1/
│   │       ├── **init**.py
│   │       └── routes.py     # API endpoints
│   ├── core/
│   │   ├── **init**.py
│   │   ├── config.py         # Environment configs
│   │   └── logging.py        # Logging setup
│   ├── services/
│   │   ├── **init**.py
│   │   ├── llm_service.py    # LLM wrapper (LangChain/OpenAI)
│   │   └── assistant_service.py # Business logic / orchestrator
│   ├── utils/
│   │   ├── **init**.py
│   │   └── helpers.py        # Reusable utilities
│   └── tests/
│       ├── **init**.py
│       └── test_routes.py    # Unit tests
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md
└── .env.example              # Example env variables

````

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/generative-ai-assistant.git
cd generative-ai-assistant
````

### 2️⃣ Create `.env` file

Copy `.env.example` into `.env` and set your environment variables:

```env
OPENAI_API_KEY=your_api_key_here
MODEL_NAME=gpt-4
```

### 3️⃣ Install dependencies (local dev)

```bash
python -m venv venv
source venv/bin/activate  # (Linux/macOS)
venv\Scripts\activate     # (Windows)

pip install --upgrade pip
pip install -r requirements.txt
```

### 4️⃣ Run locally

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API will be available at:
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Run with Docker

### Build & start services

```bash
docker-compose up --build
```

### Stop services

```bash
docker-compose down
```

---

## 📡 API Usage

### Example Request

```bash
curl -X POST "http://localhost:8000/api/v1/ask" \
-H "Content-Type: application/json" \
-d '{"query": "Tell me a fun fact about space"}'
```

### Example Response

```json
{
  "response": "Did you know that a day on Venus is longer than a year on Venus?"
}
```

---

## 🧪 Testing

Run tests with `pytest`:

```bash
pytest app/tests/ -v
```

---

## 🚀 Roadmap

* [ ] Add memory support (conversation history)
* [ ] Integrate retrieval-augmented generation (RAG)
* [ ] Multi-model support (Anthropic, LLaMA, Mistral)
* [ ] Add monitoring & observability (Prometheus, Grafana)

---

## 🤝 Contributing

1. Fork the repo
2. Create a new branch (`feature/my-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** – see [LICENSE](LICENSE) for details.

---
