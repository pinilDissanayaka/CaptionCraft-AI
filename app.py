import os
import streamlit as st
from utils.llm_handler import generate_caption

temp_file_path="temp/"

# App title
st.set_page_config(page_title="📸 CaptionCraft AI 🎨")

st.title("📸 CaptionCraft AI 🎨")
st.write("-----------------------------------------------------------------------------------------------------------") 
st.write("CaptionCraft AI is an advanced image caption generator that combines image recognition and natural language processing. With the help of LLMs for generating initial captions and RAG for refining them with contextual data, this tool produces accurate and enriched descriptions for your images! 🌟")
st.write("-----------------------------------------------------------------------------------------------------------") 


uploaded_image_files = st.file_uploader(" Upload an Images or Photos", accept_multiple_files=True)

if uploaded_image_files:
    for uploaded_image_file in uploaded_image_files:
        st.image(image=uploaded_image_file)

selected_vibe = st.selectbox(
    "Select a vibe",
    options=("Funny 😂🎉",
     "Professional 💼📊",
     "Casual 😎👕",
     "Inspirational 🌟🚀",
     "Adventurous 🏞️🌍",
     "Romantic 💕🌹",
     "Playful 😜🎈",
     "Sarcastic 🙃🖋️",
     "Minimalist ✨📏",
     "Empathetic 🤗💖",
     "Mysterious 🕵️‍♀️🖤",
     "Energetic ⚡🔥",
     "Wholesome 🍃🍂",
     "Luxurious 💎👑",
     "Nostalgic 📸💭",
     "Sad 😢💔",
     "Joke 🤣🃏",
     "Serious 🧐⚖️",
     "Cute 🥰🐾",
     "Cool 😎🔥")
)

additional_prompt=st.text_input("Additional Prompt (optional) : ", value=None)

if uploaded_image_files and selected_vibe:
    if st.button("Generate Captions"):
        with st.spinner("Thinking..."):
            generated_captions=generate_caption(vibe=selected_vibe, addition_prompt=additional_prompt, image_files=uploaded_image_files)
            st.write(generated_captions)
    




