from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import RetrievalQA
from .vector_store import get_vector_store
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


llm = GoogleGenerativeAI(model="gemini-pro")
vector_store = get_vector_store()

# Configure RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(llm, retriever=vector_store.as_retriever())

def chatbot_agent(query: str):
    """
    Processes user queries:
    - If the query contains 'call me', asks for Name, Email, and Phone Number.
    - If the query contains 'book appointment', asks for Name, Email, Phone Number, and Date.
    - Otherwise, retrieves an answer from documents and uses LLM if needed.
    """
    query_lower = query.lower()  # Convert query to lowercase for better matching

    # Handle 'call me' queries
    if "call me" in query_lower:
        return "To proceed with the call request, please provide your Name, Email, and Phone Number."

    # Handle 'book appointment' queries
    if "book appointment" in query_lower or "schedule an appointment" in query_lower:
        return "To book an appointment, please provide your Name, Email, Phone Number, and Preferred Date (YYYY-MM-DD)."

    # Retrieve answer from documents
    try:
        response = qa_chain.invoke({"query": query})  # Pass query as a dictionary
    except Exception as e:
        response = f"Error during processing: {str(e)}"

    # Fallback to LLM if response is empty or irrelevant
    if not response or "I don't know" in response:
        response = llm.invoke(f"Answer this query using your knowledge: {query}")

    return response