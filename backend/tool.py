from langchain.tools import StructuredTool
from pydantic import BaseModel
from datetime import datetime

class CallMeSchema(BaseModel):
    name: str
    email: str
    phone: str

class BookAppointmentSchema(BaseModel):
    name: str
    email: str
    phone: str
    date: str  

def call_me(data: CallMeSchema):
    """Handles user requests to receive a call within 24 hours."""
    return f"{data.name}, you will be called within 24 hours."

def book_appointment(data: BookAppointmentSchema):
    """Handles user requests to book an appointment on a specific date."""
    try:
        datetime.strptime(data.date, "%Y-%m-%d")  # Validate date format
        return f"Appointment booked for {data.name} on {data.date}."
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

# Create Structured Tools
CallMeTool = StructuredTool.from_function(func=call_me, name="call_me", args_schema=CallMeSchema)
BookAppointmentTool = StructuredTool.from_function(func=book_appointment, name="book_appointment", args_schema=BookAppointmentSchema)
