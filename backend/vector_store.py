from langchain.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from .documents_loader import load_documents
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


def get_vector_store():
    docs = load_documents()
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return Chroma.from_documents(docs, embeddings)
