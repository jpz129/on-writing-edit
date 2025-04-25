import tiktoken
from fastapi import HTTPException

encoding = tiktoken.encoding_for_model("gpt-4")

def check_token_limit(text: str, max_tokens: int = 64000):
    if len(encoding.encode(text)) > max_tokens:
        raise HTTPException(status_code=400, detail="⚠️ Input too long. Please reduce your text to under 64,000 tokens.")