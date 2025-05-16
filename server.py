

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.agent import chatbot_agent

class QueryRequest(BaseModel):
    query: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: QueryRequest):
    try:
        response = chatbot_agent(request.query)

        
        if isinstance(response, dict) and "result" in response:
            response_text = response["result"]
        else:
            response_text = str(response)

        return {"response": response_text}  

    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/call_me")
async def call_me(request: CallMeSchema):
    return {"response": f"You will be called within 24 hours. Name: {request.name}, Email: {request.email}, Phone: {request.phone}"}

@app.post("/book_appointment")
async def book_appointment(request: BookAppointmentSchema):
    return {"response": f"Appointment booked for {request.date}. Name: {request.name}, Email: {request.email}, Phone: {request.phone}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
