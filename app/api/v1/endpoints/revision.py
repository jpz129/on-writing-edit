from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.revision.service import revise_with_context

router = APIRouter()

class RevisionRequest(BaseModel):
    text: str

@router.post("/")
async def revise_text(request: RevisionRequest):
    try:
        print("✅ Received request text:", request.text)
        result = await revise_with_context(request.text)
        print("✅ Result keys returned:", list(result.keys()))
        return result
    except Exception as e:
        print("❌ Exception occurred in revise_text:", str(e))
        raise HTTPException(status_code=500, detail=str(e))