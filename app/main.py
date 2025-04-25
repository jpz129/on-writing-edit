from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from app.api.v1.endpoints import revision

app = FastAPI(title="Revise Like King")

app.include_router(revision.router, prefix="/api/v1/revise", tags=["Revision"])