from flask import Flask, request, jsonify, render_template
from modules.transcriber import get_transcript
from modules.embedder import store_transcript
from modules.retriever import retrieve_chunks
from modules.generator import generate_answer, generate_summary, generate_questions

app = Flask(__name__)

# ─── Home page ───────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


# ─── Process video ───────────────────────────────────
@app.route("/process", methods=["POST"])
def process():
    """
    Takes a YouTube video ID from the user,
    fetches transcript and stores it in ChromaDB.
    """
    data = request.get_json()
    video_id = data.get("video_id", "").strip()

    if not video_id:
        return jsonify({"error": "Video ID is required!"}), 400

    try:
        transcript = get_transcript(video_id)
        store_transcript(transcript)
        return jsonify({"message": "✅ Video processed successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ─── Summary ─────────────────────────────────────────
@app.route("/summary", methods=["GET"])
def summary():
    """Retrieve and summarize the lecture"""
    try:
        context = retrieve_chunks("summarize the lecture", n_results=5)
        result = generate_summary(context)
        return jsonify({"summary": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ─── Quiz questions ───────────────────────────────────
@app.route("/questions", methods=["GET"])
def questions():
    """Generate quiz questions from the lecture"""
    try:
        context = retrieve_chunks("key concepts and topics", n_results=5)
        result = generate_questions(context)
        return jsonify({"questions": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ─── Ask a question ───────────────────────────────────
@app.route("/ask", methods=["POST"])
def ask():
    """Answer a user's doubt from the lecture"""
    data = request.get_json()
    query = data.get("question", "").strip()

    if not query:
        return jsonify({"error": "Question cannot be empty!"}), 400

    try:
        context = retrieve_chunks(query)
        answer = generate_answer(query, context)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ─── Run ─────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)