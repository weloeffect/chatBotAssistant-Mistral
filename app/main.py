from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.nlp import generate_response

app = FastAPI()

# Define a Pydantic model for the user input
class ChatInput(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Chatbot Assistant API"}

@app.post("/chat/")
async def chat(input: ChatInput):
    # Use the NLP function to generate a response
    try:
        response = generate_response(input.query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
