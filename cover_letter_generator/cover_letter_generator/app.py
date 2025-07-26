import os
import tempfile
import streamlit as st
from dotenv import load_dotenv
from generator import generate_cover_letter
from utils import extract_text_from_pdf

# Load environment variables
load_dotenv()

st.set_page_config(page_title="Cover Letter Generator", layout="wide")
st.title("📝 LLM-Powered Cover Letter Generator")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
if uploaded_file:
    # Save uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    # Extract text from PDF
    resume_text = extract_text_from_pdf(tmp_path)

    if resume_text.strip() == "":
        st.error("❌ Could not extract text from PDF. Please upload a valid resume PDF.")
    else:
        if st.button("Generate Cover Letter"):
            with st.spinner("Generating cover letter..."):
                try:
                    cover_letter = generate_cover_letter(resume_text)
                    st.subheader("✅ Generated Cover Letter")
                    st.write(cover_letter)
                except Exception as e:
                    st.error(f"Error generating cover letter: {e}")
