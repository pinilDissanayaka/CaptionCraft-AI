from utils.config import get_llm
from utils.image_handler import get_image_descriptions
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


def generate_caption(vibe:list, addition_prompt:str, image_files):
    image_descriptions=get_image_descriptions(image_files=image_files)
    if addition_prompt:    
        caption_generate_prompt_template="""
        Based on the following list of image descriptions, create a 5 captions that captures the essence of the image. The caption should match the following vibe: {VIBE} 
        and include relevant emojis to enhance the message. Additionally, consider the following prompts for extra context: {ADDITIONAL_PROMPT}.

        Here are the image descriptions:
            {IMAGE_DESCRIPTIONS}
        Generate a {VIBE} caption that is concise, engaging, and reflective of the image. Make sure to incorporate the right amount of emojis to fit the tone and enhance the caption.
        """
    
        caption_generate_prompt=ChatPromptTemplate.from_template(template=caption_generate_prompt_template)
    
        llm=get_llm()
    
        caption_generate_chain=(
            {"VIBE": RunnablePassthrough(), "ADDITIONAL_PROMPT": RunnablePassthrough(), "IMAGE_DESCRIPTIONS": RunnablePassthrough()} |
            caption_generate_prompt |
            llm |
            StrOutputParser()
        )

    
        generated_captions=caption_generate_chain.invoke({"VIBE": vibe, "ADDITIONAL_PROMPT": addition_prompt, "IMAGE_DESCRIPTIONS": image_descriptions})
    
    else:
        caption_generate_prompt_template="""
        Based on the following list of image descriptions, create a 5 captions that captures the essence of the image. The caption should match the following vibe: {VIBE} 
        and include relevant emojis to enhance the message.

        Here are the image descriptions:
            {IMAGE_DESCRIPTIONS}
        Generate a {VIBE} caption that is concise, engaging, and reflective of the image. Make sure to incorporate the right amount of emojis to fit the tone and enhance the caption.
        """
    
        caption_generate_prompt=ChatPromptTemplate.from_template(template=caption_generate_prompt_template)
    
        llm=get_llm()
    
        caption_generate_chain=(
            {"VIBE": RunnablePassthrough(), "IMAGE_DESCRIPTIONS": RunnablePassthrough()} |
            caption_generate_prompt |
            llm |
            StrOutputParser()
        )

    
        generated_captions=caption_generate_chain.invoke({"VIBE": vibe, "IMAGE_DESCRIPTIONS": image_descriptions})
    
    return generated_captions