from modules.transcriber import get_transcript
from modules.embedder import store_transcript
from modules.retriever import retrieve_chunks
from modules.generator import generate_answer, generate_summary, generate_questions

video_id = "UZDiGooFs54"

print("🎬 Fetching transcript...")
transcript = get_transcript(video_id)

print("🧠 Storing in ChromaDB...")
store_transcript(transcript)

# Test 1 — Summary
print("\n📝 SUMMARY:")
context = retrieve_chunks("summarize the lecture", n_results=5)
print(generate_summary(context))

# Test 2 — Questions
print("\n❓ QUESTIONS:")
print(generate_questions(context))

# Test 3 — Doubt Q&A
print("\n💬 DOUBT Q&A:")
query = "what is a transformer?"
context = retrieve_chunks(query)
print(generate_answer(query, context))