import os
import yaml
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
os.environ['PINECONE_API_KEY']=os.getenv('PINECORN_API_KEY')
os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ["GOOGLE_API_KEY"]=os.getenv('GOOGLE_API_KEY')
os.environ["GOOGLE_PROJECT_ID"]=os.getenv('GOOGLE_PROJECT_ID')


with open("config.yaml", "r") as file:
    configuration=yaml.safe_load(file)


def get_embedding_model():
    return GoogleGenerativeAIEmbeddings(model=configuration["embedding_model"])

def get_vision_model()->str:
    return configuration["vision_model"]

def get_llm():
    return ChatGroq(model=configuration["llm"]["model"],
                          temperature=configuration["llm"]["temperature"],
                            max_tokens=configuration["llm"]["max_tokens"],
                            timeout=configuration["llm"]["timeout"])

def get_vision_prompt():
    return configuration['vision_prompt']


