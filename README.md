# 📚 Revise Like King — An AI Writing Assistant Inspired by Stephen King

Sharpen your writing the King way (this tool edited the README btw).

This project uses a FastAPI backend, LangChain, OpenAI’s GPT-4, and Pinecone for vector search to revise your text in line with *On Writing*. Deployed on Google Cloud Run, it’s fast, containerized, and ready to scale.



---

## ✨ What It Does

1. 📝 **Paste your passage** into the Gradio front end.
2. 🧠 **An LLM analyzes** your words and crafts a search query.
3. 📖 **Relevant advice** from a vectorized copy of *On Writing* is retrieved via Pinecone.
4. 🧙 **GPT-4 rewrites** your text using King’s principles.
5. ⚡ **You get it back** — clearer, tighter, stronger.

---

## 💻 Tech Stack

- **FastAPI** — modular, scalable backend in Python
- **LangChain** — orchestrates query → retrieval → revision
- **OpenAI GPT-4** — the creative engine
- **Pinecone** — semantic vector store of *On Writing*
- **Gradio** — simple, interactive front end
- **Docker** — for portability
- **Google Cloud Run** — serverless scale

---

## 🚀 Try the Demo

Test it locally:

```bash
python test_gradio.py
```

> Your Gradio app will run at `http://localhost:7860`.

Access the FastAPI backend at:

```
https://on-writing-app-<your-run-id>.a.run.app/docs
```

---

## 🛠️ Local Dev Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/yourname/on-writing-edit.git
   cd on-writing-edit
   ```

2. Set up your environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Add your keys in a `.env` file:
   ```
   OPENAI_API_KEY=your-openai-key
   PINECONE_API_KEY=your-pinecone-key
   ```

4. Start locally:
   ```bash
   PYTHONPATH=. uvicorn app.main:app --reload
   ```

Visit `http://localhost:8000/docs` to use the API.

---

## 🐳 Docker & Cloud Run

Build and deploy:

```bash
docker buildx build --platform linux/amd64 -t on-writing-app .
docker tag on-writing-app us-central1-docker.pkg.dev/YOUR_PROJECT/on-writing-repo/on-writing-app
docker push us-central1-docker.pkg.dev/YOUR_PROJECT/on-writing-repo/on-writing-app

gcloud run deploy on-writing-app \
  --image=us-central1-docker.pkg.dev/YOUR_PROJECT/on-writing-repo/on-writing-app \
  --platform=managed \
  --region=us-central1 \
  --allow-unauthenticated \
  --port=8000 \
  --set-env-vars=OPENAI_API_KEY=your-key,PINECONE_API_KEY=your-key
```

---

## 🧠 Why This Exists

Created as a portfolio project by [Juan Pablo](https://github.com/jpz129), this app blends literary style, practical AI, and production-ready infrastructure.

It’s made for clarity, brevity, and revision — in true King fashion. Omit needless words. Sharpen every line. Write, revise, repeat.