

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai
import fitz  # PyMuPDF

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input_text, pdf_content, prompt):
    """Call Google Gemini AI for response."""
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([input_text, pdf_content[0], prompt])
    return response.text

def input_pdf_text(upload_file):
    """Extract text from uploaded PDF."""
    if upload_file is not None:
        pdf_bytes = upload_file.read()
        pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        full_text = ""
        for page in pdf_doc:
            full_text += page.get_text()
        return full_text.strip()
    else:
        raise FileNotFoundError("No file found")
    
def response_card(title, content, card_color="#ffffff", border_color="#4CAF50"):
    """
    Display AI response in a modern, clean card.
    """
    st.markdown(
        f"""
        <div style="
            background-color: {card_color};
            border-left: 6px solid {border_color};
            padding: 20px;
            border-radius: 12px;
            margin-top: 15px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        ">
            <h3 style="color: #ffffff; margin-bottom: 12px; font-family: 'Segoe UI', sans-serif;">{title}</h3>
            <div style="
                color: #ffffff;
                font-size: 15px;
                line-height: 1.6;
                white-space: pre-line;
                font-family: 'Segoe UI', sans-serif;
            ">{content}</div>
        </div>
        """,
        unsafe_allow_html=True
    )




st.set_page_config(page_title="AI ATS Resume Matcher", page_icon="🤖", layout="wide")

st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>AI Resume Matcher 🤖</h1>
    <p style='text-align: center; color: grey;'>Smart ATS Tracker that compares your resume with a job description.</p>
    """,
    unsafe_allow_html=True
)

# Two-column layout: Job Description | Resume Upload
col1, col2 = st.columns([2, 1])

with col1:
    input_text = st.text_area(
        "📄 Job Description", 
        key="input", 
        height=300, 
        placeholder="Paste the job description here..."
    )

with col2:
    upload_file = st.file_uploader("📂 Upload Resume (PDF)", type=["pdf"], key="upload")
    if upload_file:
        st.success("✅ Resume uploaded successfully")

col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    submit1 = st.button("🔍 Resume Review", use_container_width=True)
with col_btn2:
    submit3 = st.button("📊 Percentage Match", use_container_width=True)

# AI Prompts

input_prompt1 = """
You are an experienced Technical Human Resource Manager. 
Review the provided resume against the job description.

Provide a **very concise evaluation** in **bullet points**, using **1 line per point**, with no long paragraphs. Only include the most important highlights.

Format exactly like this:

Overall Fit: <one short sentence>

Strengths:
- <most important skill/experience>
- <most important skill/experience>

Weaknesses / Gaps:
- <most critical gap>
- <most critical gap>

Suggestions:
- <top improvement>
- <top improvement>

Limit each section to **2 bullet points max**.
"""

input_prompt3 = """
You are an ATS helper reviewing a resume against a job description.
Provide output in **very simple, plain language** that anyone can understand.
Give output in **exactly 3–4 short lines**, including:

1. Percentage Match: <number>% 
2. Suggestions to improve the resume for ATS: short, actionable points with a **tiny example or hint**.
"""

# -----------------------------
# Button Actions
# -----------------------------

if submit1:
    if upload_file is not None:
        resume_text = input_pdf_text(upload_file)
        response = get_gemini_response(input_prompt1, resume_text, input_text)
        response_card("📑 Resume Analysis", response, "#121313")
    else:
        st.warning("⚠️ Please upload the resume")

# elif submit3:
#     if upload_file is not None:
#         resume_text = input_pdf_text(upload_file)
#         response = get_gemini_response(input_prompt3, resume_text, input_text)
#         response_card("📊 ATS Match Result", response, "#121313")
#     else:
#         st.warning("⚠️ Please upload the resume")

elif submit3:
    if upload_file is not None:
        resume_text = input_pdf_text(upload_file)
        response = get_gemini_response(input_prompt3, resume_text, input_text)

        # Extract percentage from response
        import re
        import plotly.graph_objects as go

        match = re.search(r"Percentage Match:\s*(\d+)%", response)
        percentage = int(match.group(1)) if match else 0

        st.subheader("📊 ATS Match Result")

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=percentage,
            number={'suffix': "%"},
            gauge={'axis': {'range': [0, 100]},
                   'bar': {'color': "#4CAF50"},
                   'bgcolor': "lightgray"}
        ))

        fig.update_layout(width=300, height=300)
        st.plotly_chart(fig)

        response_card("Suggestions", response, "#121313")
    else:
        st.warning("⚠️ Please upload the resume")



# Custom Styling

st.markdown(
    """
    <style>
    .stTextArea textarea {background-color: #ffffff; border-radius: 10px;color:black}
    .stFileUploader {border: 1px dashed #4CAF50; padding: 10px; border-radius: 10px;}
    </style>
    """,
    unsafe_allow_html=True
)




# from dotenv import load_dotenv
# load_dotenv()

# import streamlit as st
# import os
# from PIL import Image
# import pdf2image
# import google.generativeai as genai
# import io       
# import base64    
# import fitz


# # Configure Google Generative AI
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



# # Function to get Gemini AI response
# def get_gemini_response(input_text, pdf_content, prompt):
#     model = genai.GenerativeModel('gemini-2.5-flash')
#     response = model.generate_content([input_text, pdf_content[0], prompt])
#     return response.text

# # Function to convert PDF to base64 images
# import fitz  # PyMuPDF

# def input_pdf_text(upload_file):
#     if upload_file is not None:
#         pdf_bytes = upload_file.read()
#         pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        
#         # Extract text from all pages
#         full_text = ""
#         for page in pdf_doc:
#             full_text += page.get_text()
        
#         return full_text.strip()
#     else:
#         raise FileNotFoundError("No file found")


# # Streamlit UI
# st.set_page_config(page_title="AI Resume Matcher", page_icon=":robot_face:")
# st.header("ATS Tracking System")

# input_text = st.text_area("Job Description", key="input")
# upload_file = st.file_uploader("Upload Resume (PDF)....", type=["pdf"], key="upload")

# # Store PDF content in session_state to avoid reading multiple times
# if 'pdf_content' not in st.session_state:
#     if upload_file is not None:
#         try:
#             st.session_state.pdf_content = input_pdf_text(upload_file)
#             st.success("PDF Uploaded Successfully")
#         except Exception as e:
#             st.error(f"Error processing PDF: {e}")

# # Buttons
# submit1 = st.button("Tell Me About the Resume")
# submit3 = st.button("Percentage Match")

# # Prompts
# input_prompt1 = """
# You are an experienced Technical Human Resource Manager. 
# Review the provided resume against the job description.

# Provide a **very concise evaluation** in **bullet points**, using **1 line per point**, with no long paragraphs. Only include the most important highlights.

# Format exactly like this:

# Overall Fit: <one short sentence>

# Strengths:
# - <most important skill/experience>
# - <most important skill/experience>

# Weaknesses / Gaps:
# - <most critical gap>
# - <most critical gap>

# Suggestions:
# - <top improvement>
# - <top improvement>

# Limit each section to **2 bullet points max**.
# """



# input_prompt3 = """
# You are an ATS helper reviewing a resume against a job description.
# Provide output in **very simple, plain language** that anyone can understand.
# Give output in **exactly 3–4 short lines**, including:

# 1. Percentage Match: <number>%
# 2. Suggestions to improve the resume for ATS: short, actionable points with a **tiny example or hint**.

# Use examples that a beginner can understand. Avoid technical jargon.

# Example output:

# Percentage Match: 70% 

# Suggestions: (in new line)
# - Add the tools you know. Example: "Used Python and Excel to analyze data."
# - Show your projects. Example: "Built a sales prediction model."
# - Include results or numbers. Example: "Increased accuracy by 10%."
# - Mention teamwork. Example: "Worked with 3 team members to complete a project."
# """

# # Button actions
# if submit1:
#     if upload_file is not None:
#         resume_text = input_pdf_text(upload_file)
#         response = get_gemini_response(input_prompt1, resume_text, input_text)
#         st.subheader("The Response is:")
#         st.write(response)
#     else:
#         st.warning("Please upload the resume")

# elif submit3:
#     if upload_file is not None:
#         resume_text = input_pdf_text(upload_file)
#         response = get_gemini_response(input_prompt3, resume_text, input_text)
#         st.subheader("The Response is:")
#         st.write(response)
#     else:
#         st.warning("Please upload the resume")