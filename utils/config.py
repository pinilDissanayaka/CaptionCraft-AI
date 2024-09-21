import os
import yaml
import streamlit as st
import logging
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_groq.chat_models import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from groq import Groq
import base64

load_dotenv()

os.environ['GOOGLE_API_KEY']=os.getenv('GOOGLE_API_KEY')
os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')
os.environ["GOOGLE_PROJECT_ID"]=os.getenv('GOOGLE_PROJECT_ID')

os.environ['GOOGLE_API_KEY']=st.secrets['GOOGLE_API_KEY']
os.environ['GROQ_API_KEY']=st.secrets['GROQ_API_KEY']
os.environ["GOOGLE_PROJECT_ID"]=st.secrets['GOOGLE_PROJECT_ID']


with open("utils/config.yaml", "r") as file:
    configuration=yaml.safe_load(file)


def get_embedding_model():
    return GoogleGenerativeAIEmbeddings(model=configuration["embedding_model"])

def get_vision_model()->str:
    return configuration["vision_model"]

def get_llm():
    return ChatGroq(model=configuration["llm"]["model"],
                          temperature=configuration["llm"]["temperature"],
                            max_tokens=None,
                            timeout=None)

def get_vision_prompt():
    return configuration['vision_prompt']


