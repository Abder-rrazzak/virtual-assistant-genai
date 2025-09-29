from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag_pipeline import generate_response

router = APIRouter()

class ChatRequest(BaseModel):
    session_id: str
    message: str

class ChatResponse(BaseModel):
    answer: str
    sources: list[str]
    confidence: float

@router.post("/", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    answer, sources, confidence = await generate_response(req.session_id, req.message)
    return ChatResponse(answer=answer, sources=sources, confidence=confidence)
