import os
from pinecone import Pinecone
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

def get_vectorstore():
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    index = pc.Index("on-writing-index")
    embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")
    return PineconeVectorStore(index=index, embedding=embedding_model)