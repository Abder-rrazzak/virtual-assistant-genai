from fastapi import FastAPI
from app.routers import chat

app = FastAPI(title="Generative AI Virtual Assistant")

# Include routes
app.include_router(chat.router, prefix="/chat", tags=["chat"])

@app.get("/")
def root():
    return {"status": "ok", "message": "Virtual Assistant is running"}
