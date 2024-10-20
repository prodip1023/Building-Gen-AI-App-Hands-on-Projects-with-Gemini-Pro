# Loading all the environment variables
from dotenv import load_dotenv
load_dotenv()


import streamlit as st
import os
import google.generativeai as genai

# os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get response
# model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)
    return response.text


# Initialize our streamlit app
st.set_page_config(page_title='Q&A Application')
st.header("Gemini LLM Application")
input=st.text_input("Input: ",key="input")
submit = st.button("Ask the question")

# When submit is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
