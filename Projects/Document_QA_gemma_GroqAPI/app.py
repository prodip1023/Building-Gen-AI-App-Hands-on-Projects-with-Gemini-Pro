import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
# Load the GROQ and Google API key from the .env file
groq_api_key = os.getenv("GROQ_API_KEY")
os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")

st.title("Gemma Model Document Q&A")

llm = ChatGroq(groq_api_key=groq_api_key,model='gemma-7b-it')
prompt = ChatPromptTemplate.from_template( 
"""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Questions: {input}
"""
)

def vector_embedding():

    if "vectors" not in st.session_state:
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001") # embedding model
        st.session_state.loader = PyPDFDirectoryLoader("./Data") # Data Ingestion
        st.session_state.docs = st.session_state.loader.load() # Documentloading
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,chunk_overlap=200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs)
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings)


prompt1 = st.text_input("What you want to ask from the documents?")

if st.button("Creating vector store"):
    vector_embedding()
    st.write("Vectore Store DB Is Ready")


import time
if prompt1:
    document_chain = create_stuff_documents_chain(llm,prompt)
    retriever = st.session_state.vectors.as_retriever()
    retriever_chain = create_retrieval_chain(retriever, document_chain)

    start = time.process_time()
    response = retriever_chain({'input':prompt1})
    st.swite(response['answer'])

    # with a streamlit expander 
    with st.expander("Document Similarity Search"):
       # Find the relevant chunks
       for i,doc in enumerate(response['context']):
           st.write(doc.page_content)
           st.write("------------------------------------")

