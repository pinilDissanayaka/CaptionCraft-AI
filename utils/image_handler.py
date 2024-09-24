import os
import base64
from utils.config import get_vision_prompt, get_vision_model
from groq import Groq
from tempfile import TemporaryDirectory
import logging

temp_dir="/temp"


def save_img_dir(uploaded_files):
    for upload_file in uploaded_files:
        dir=os.path.join(temp_dir, upload_file.name)
        pass
    


def covert_image_to_base64(image_file):
    image_encoding=base64.encode(image_file.read()).decode('utf-8')
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
        

def get_image_descriptions(image_files):
    
    image_descriptions=[]
    
    for image_file in image_files:
        #image_encoding=covert_image_to_base64(image_file=image_file.read())
        image_description=covert_image_to_text(image_encoding=image_file)

        image_descriptions.append(image_description)
        
    return image_descriptions

