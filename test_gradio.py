import gradio as gr
import requests

BASE_URL = "https://on-writing-app-2352728448.us-central1.run.app/api/v1/revise/"

def call_revision_api(text):
    try:
        response = requests.post(
            BASE_URL,
            headers={"Content-Type": "application/json"},
            json={"text": text},
            timeout=20
        )
        if response.status_code == 200:
            return response.json().get("revised_passage", "✅ Success but no text returned")
        else:
            return f"❌ Error: {response.status_code} - {response.json().get('detail', 'No detail')}"
    except Exception as e:
        return f"⚠️ Request failed: {str(e)}"

gr.Interface(
    fn=call_revision_api,
    inputs=gr.Textbox(lines=10, label="Original Text"),
    outputs=gr.Textbox(lines=10, label="Revised Text"),
    title="📝 Revise Like King — Live Demo",
    description=(
        "This app takes your passage and rewrites it using principles from *On Writing* by Stephen King.\n\n"
        "Under the hood, your text is sent to a FastAPI application deployed on Google Cloud Run. "
        "That app uses LangChain with OpenAI (GPT-4) and Pinecone to retrieve relevant writing advice "
        "from King's book, then returns an AI-edited version of your original text.\n\n"
        "Paste a paragraph or two and see how it gets 'King-ified'!"
    ),
    flagging_mode="never"
).launch()