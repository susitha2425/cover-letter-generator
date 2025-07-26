# generator.py
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

def generate_cover_letter(resume_text: str) -> str:
    """
    Generates a cover letter based solely on the provided resume text using Groq's LLM.
    """
    llm = ChatGroq(
        temperature=0.7,
        model="llama3-8b-8192",  # or "mixtral-8x7b-32768"
        api_key=os.getenv("GROQ_API_KEY")
    )

    system_prompt = (
        "You are an expert cover letter writer. "
        "Write a professional cover letter based only on the candidate's resume. "
        "Do not include any job description or external information."
    )

    human_prompt = f"Generate a cover letter using the following resume:\n{resume_text}"

    response = llm([
        SystemMessage(content=system_prompt),
        HumanMessage(content=human_prompt)
    ])
    return response.content
