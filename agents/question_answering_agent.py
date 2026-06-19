import os
import google.generativeai as genai
from dotenv import load_dotenv

from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent.parent / "backend" / ".env")
print(os.getenv("GEMINI_API_KEY"))

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def answer_question(question, summary, insights, research_summary):

    prompt = f"""
You are ARIA AI Data Scientist.

Dataset Summary:
{summary}

Insights:
{insights}

Research Summary:
{research_summary}

User Question:
{question}

Give a professional data science answer.
Explain reasoning clearly.
"""

    response = model.generate_content(prompt)

    return response.text