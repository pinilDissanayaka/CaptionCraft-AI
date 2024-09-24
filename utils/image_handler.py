import os
import base64
from utils.config import get_vision_prompt, get_vision_model
from groq import Groq
from tempfile import TemporaryDirectory
import logging


def covert_image_to_base64(image_file):
    image_encoding=base64.b64encode(image_file).decode('utf-8')
    return image_encoding


def covert_image_to_text(image_encoding):
    try:
        client = Groq()

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": get_vision_prompt()},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_encoding}",
                            },
                        },
                    ],
                }
            ],
            model=get_vision_model(),
        )   

        return chat_completion.choices[0].message.content
    except Exception as e:
        logging.exception(e)
        

def get_image_descriptions(saved_images):
    
    image_descriptions=[]
    
    for saved_image in saved_images:
        with open(saved_image, "rb") as image_file:
            image_encoding=covert_image_to_base64(image_file=image_file.read())
            
        image_description=covert_image_to_text(image_encoding=image_encoding)
        image_descriptions.append(image_description)
        
        if os.path.exists(saved_image):
                os.remove(saved_image)
        
    return image_descriptions

def save_image(original_image_file):
    
    temp_dir="temp"
    
    image_path=os.path.join(temp_dir, original_image_file.name)
    
    with open(image_path, "wb") as image_file:
        image_file.write(original_image_file.getbuffer())

    return image_path
    
    
    