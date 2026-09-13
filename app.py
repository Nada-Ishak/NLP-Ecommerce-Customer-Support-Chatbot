from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="E-commerce Customer Support Chatbot",
    version="1.0"
)

class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "E-commerce Customer Support Chatbot API",
        "status": "running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    result = chatbot(request.message)

    return result