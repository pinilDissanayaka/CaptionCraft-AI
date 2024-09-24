import os
import streamlit as st
from utils.llm_handler import generate_caption
from utils.image_handler import save_image



# App title
st.set_page_config(page_title="📸 CaptionCraft AI 🎨")

st.title("📸 CaptionCraft AI 🎨")
st.write("-----------------------------------------------------------------------------------------------------------") 
st.write("CaptionCraft AI is an advanced image caption generator that combines image recognition and natural language processing. With the help of LLMs for generating initial captions and RAG for refining them with contextual data, this tool produces accurate and enriched descriptions for your images! 🌟")
st.write("-----------------------------------------------------------------------------------------------------------") 


uploaded_image_files = st.file_uploader(" Upload an Images or Photos :", accept_multiple_files=True, type=["jpg", "jpeg", "png", "gif"])

saved_images=[]

if uploaded_image_files:
    for uploaded_image_file in uploaded_image_files:
        saved_image=save_image(original_image_file=uploaded_image_file)
        saved_images.append(saved_image)
        st.image(image=saved_image)

selected_vibe = st.selectbox(
    "Select a vibe :",
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
            generated_captions=generate_caption(vibe=selected_vibe, addition_prompt=additional_prompt, saved_images=saved_images)
            st.write(generated_captions)
    




