import chromadb
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # loads your API key from .env

client = OpenAI()  # connects to OpenAI

# Create a ChromaDB client that saves to disk
chroma_client = chromadb.PersistentClient(path="./chroma_db")

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list:
    """
    Split text into overlapping chunks.
    chunk_size = how many characters per chunk
    overlap    = how many characters to repeat between chunks
    """
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap  # step back a little for overlap

    return chunks

def get_embedding(text: str) -> list:
    """Convert a piece of text into a vector (list of numbers)"""
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"  # cheap and very good
    )
    return response.data[0].embedding

def store_transcript(transcript: str, collection_name: str = "lecture"):
    """
    Chunk the transcript, embed each chunk,
    and store everything in ChromaDB.
    """
    # Always start fresh — delete old collection if exists
    try:
        chroma_client.delete_collection(collection_name)
    except:
        pass  # if it doesn't exist, no problem

    collection = chroma_client.create_collection(collection_name)

    chunks = chunk_text(transcript)

    print(f"📦 Storing {len(chunks)} chunks in ChromaDB...")

    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[f"chunk_{i}"]
        )

    print("✅ All chunks stored!")