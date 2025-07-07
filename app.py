import streamlit as st
import PyPDF2
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-2.5-pro')
    response = model.generate_content(input)
    return response.text



def input_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""  
        
    return text



## Prompt Template
input_prompt = """
Hey Act Like a skilled or very experienced ATS (Applicant Tracking System)
with a deep understanding of tech fields like Software Engineering, Data Science, Data Analysis, and Big Data Engineering. 
Your task is to evaluate the resume based on the given job description.

You must consider the job market is very competitive, and provide the best assistance for improving the resume. 
Assign the percentage match based on JD and highlight the missing keywords with high accuracy.

resume: {text}
description: {jd}

I want the response in one single JSON-like string using the format:
{"JD Match": "%", "MissingKeywords": [], "Profile Summary": ""}
"""



## Streamlit App
st.set_page_config(page_title="ATS Resume Expert")

st.header("ATS Tracking System")

jd = st.text_area("Paste the Job Description: ", key='input')

uploaded_file = st.file_uploader("Upload your resume(PDF)...", type=['pdf'], help="Please upload the resume")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt)
        st.subheader("Response: ")
        st.write(response)