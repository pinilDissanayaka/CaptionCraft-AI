import os
import yaml
import streamlit as st
from langchain_groq.chat_models import ChatGroq
from groq import Groq


os.environ['GROQ_API_KEY']=st.secrets['GROQ_API_KEY']


with open("utils/config.yaml", "r") as file:
    configuration=yaml.safe_load(file)

def get_vision_model()->str:
    return configuration["vision_model"]

def get_llm():
    return ChatGroq(model=configuration["llm"]["model"],
                          temperature=configuration["llm"]["temperature"],
                            max_tokens=None,
                            timeout=None)

def get_vision_prompt():
    return configuration['vision_prompt']


