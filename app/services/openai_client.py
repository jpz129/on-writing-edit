import os
from langchain_openai import ChatOpenAI

def get_openai_llm():
    return ChatOpenAI(model_name="gpt-4.1-2025-04-14")

def get_openai_llm_streaming(callbacks=[]):
    return ChatOpenAI(model_name="gpt-4.1-2025-04-14", streaming=True, callbacks=callbacks)