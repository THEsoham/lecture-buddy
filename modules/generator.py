from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def generate_answer(query: str, context: str) -> str:
    """
    Given a user query and retrieved context chunks,
    ask the LLM to generate a helpful answer.
    """
    prompt = f"""You are a helpful assistant for understanding lecture content.
Use ONLY the context provided below to answer the question.
If the answer is not in the context, say "I couldn't find that in the lecture."

CONTEXT:
{context}

QUESTION:
{query}

ANSWER:"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3  # low = more focused, less creative
    )

    return response.choices[0].message.content


def generate_summary(context: str) -> str:
    """Generate a clean summary of the lecture"""

    prompt = f"""You are a helpful assistant. 
Summarize the following lecture content in clear, simple bullet points.
Cover the main ideas and key concepts.

LECTURE CONTENT:
{context}

SUMMARY:"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


def generate_questions(context: str) -> str:
    """Generate quiz questions from the lecture"""

    prompt = f"""You are a helpful assistant.
Based on the lecture content below, generate 5 multiple choice questions.
Format each question like this:

Q1. Question here?
a) Option A
b) Option B
c) Option C
d) Option D
Answer: a)

LECTURE CONTENT:
{context}

QUESTIONS:"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    return response.choices[0].message.content