import os
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents():
    loader = DirectoryLoader("documents", glob="travel.txt")
    docs = loader.load()
    
    # Split text for efficient retrieval
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return text_splitter.split_documents(docs)
