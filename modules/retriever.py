import chromadb
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
chroma_client = chromadb.PersistentClient(path="./chroma_db")

def get_embedding(text: str) -> list:
    """Convert query text into a vector"""
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    return response.data[0].embedding

def retrieve_chunks(query: str, n_results: int = 3) -> str:
    """
    Take a user query, embed it, search ChromaDB
    for the most similar chunks, return them as text.
    """
    collection = chroma_client.get_collection("lecture")

    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    # results["documents"] is a list of lists — flatten it
    chunks = results["documents"][0]

    # Join all retrieved chunks into one block of context
    context = "\n\n".join(chunks)

    return context