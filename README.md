# 🎓 Lecture Buddy

An AI-powered YouTube lecture assistant that helps you learn smarter.
Paste a YouTube video ID and instantly get a summary, quiz questions, and answers to your doubts — all powered by RAG (Retrieval-Augmented Generation).

---

## ✨ Features

- 📝 **Smart Summary** — Get a clean bullet-point summary of any lecture
- ❓ **Auto Quiz** — Generate multiple choice questions to test your understanding
- 💬 **Ask a Doubt** — Ask anything about the lecture and get an answer grounded in the video content
- 🧠 **RAG Architecture** — Transcript is chunked, embedded, and stored in ChromaDB for accurate retrieval
- ⚡ **Fast & Lightweight** — Built with Flask, OpenAI, and ChromaDB

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Frontend | HTML, CSS, Vanilla JS |
| Backend | Flask (Python) |
| LLM | OpenAI GPT-4o-mini |
| Embeddings | OpenAI text-embedding-3-small |
| Vector DB | ChromaDB |
| Transcript | youtube-transcript-api |
| Package Manager | uv |
| Deployment | Render |

---

## 🏗️ Architecture
```
YouTube Video ID
      ↓
Fetch Transcript (youtube-transcript-api)
      ↓
Chunk + Embed (OpenAI embeddings)
      ↓
Store in ChromaDB
      ↓
User Query → Embed → Retrieve relevant chunks
      ↓
LLM generates Summary / Quiz / Answer
```

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/THEsoham/lecture-buddy.git
cd lecture-buddy
```

### 2. Install dependencies
```bash
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv add flask openai chromadb youtube-transcript-api python-dotenv gunicorn
```

### 3. Set up environment variables
Create a `.env` file in the root folder:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Run the app
```bash
uv run app.py
```

Open `http://127.0.0.1:5000` in your browser!

---

## 📁 Project Structure
```
lecture-buddy/
│
├── app.py                  # Flask routes
├── modules/
│   ├── transcriber.py      # Fetches YouTube transcript
│   ├── embedder.py         # Chunks + stores in ChromaDB
│   ├── retriever.py        # Retrieves relevant chunks
│   └── generator.py        # LLM response generation
├── templates/
│   └── index.html          # Frontend UI
├── static/
│   ├── style.css           # Styling
│   └── main.js             # Frontend logic
├── pyproject.toml          # uv dependencies
└── .env                    # API keys (never commit this!)
```

---

## ⚠️ Important Notes

- Never commit your `.env` file — it contains your secret API key!
- The app works best with YouTube videos that have auto-generated or manual captions
- One video is processed at a time — loading a new video replaces the previous one

---

## 🙋 How to Use

1. Find a YouTube lecture video
2. Copy just the **video ID** from the URL (e.g. `UZDiGooFs54` from `youtube.com/watch?v=UZDiGooFs54`)
3. Paste it in the app and hit **Let's Go!**
4. Wait for processing (~15-30 seconds)
5. Switch between **Summary**, **Quiz**, and **Ask a Doubt** tabs!

---

## 👨‍💻 Built by

**Soham** — built step by step, learning along the way 🚀

---

## 📄 License

MIT License — feel free to use, modify, and share!
