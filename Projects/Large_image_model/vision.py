# Loading all the environment variables
from dotenv import load_dotenv
load_dotenv()


import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


# os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    if input!= "":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize our streamlit app
st.set_page_config(page_title='Image Application')
st.header("Gemini Image LLM Application")
input=st.text_input("Input prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Tell me about the image")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)