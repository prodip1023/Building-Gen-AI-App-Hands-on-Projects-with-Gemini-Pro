# Loading all the environment variables from .env
from dotenv import load_dotenv
load_dotenv()


import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro Vision
def gen_gemini_response(input,image,prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input,image[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")



# Initialize our streamlit app
st.set_page_config(page_title='MultiLanguage Invoice Extractor Application')
st.header("MultiLanguage Invoice Extractor Application")
input=st.text_input("Input prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice..", type=["jpg", "jpeg", "png"])
image = ''
if uploaded_file is not None :
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit = st.button("Tell me about the invoice")

input_prompts = """
You are an expert in understanding invoices.We will upload a image as invoice
and you will have to answer any questions based on the upload invoice image

"""

# If submit button is clicked
if submit:
    image_data = input_image_details(uploaded_file)
    response = gen_gemini_response(input, image_data, input_prompts)
    st.subheader("The Response is")
    st.write(response)


