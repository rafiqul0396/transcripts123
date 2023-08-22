
import openai
import streamlit as st
import pandas as pd
from io import StringIO
import time
from datetime import datetime
import  threading
from option import Answer_outPut
import streamlit as st
import whisper
from tempfile import NamedTemporaryFile
from io import BytesIO
import os
# To split our transcript into pieces
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Our chat model. We'll use the default which is gpt-3.5-turbo
from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from base_prompt import *
from chat_prompt_map import *


def main():
    st.title("TransScript Sentiment Analysis")
    
    start=time.time()
    audio = st.file_uploader("Upload an audio file", type=["mp3"])

    option = st.selectbox(
    'Select option from dropdown?',
    ('sentiment', 'one_sentence', 'bullet_points','short','long','extraction','action_item','find_person'))
    text=""
    if audio is not None:
        with NamedTemporaryFile(suffix="mp3") as temp:
            temp.write(audio.getvalue())
            temp.seek(0)
            result = openai.Audio.transcribe("whisper-1", audio,api_key="pls insert the openai api key", verbose=True)
            st.markdown('**Transcripts:**.')
            st.text_area(label="Output Data:", value=result['text'], height=350)
            # st.write(result["text"])
            
            if st.button("Search"):

                content = result["text"]
                
                text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n"], chunk_size=2000, chunk_overlap=250)
                texts = text_splitter.create_documents([content])
                llm = ChatOpenAI(model="gpt-3.5-turbo",api_key="pls insert the openai api key",temperature=0)
                chat_prompt_map1=chat_promptMap()
                chat_prompt_combine1=chat_prompt_combine()
                chain = load_summarize_chain(llm,
                                chain_type="map_reduce",
                                map_prompt=chat_prompt_map1,
                                combine_prompt=chat_prompt_combine1,
                                verbose=True
                                )
                summary_output_options = Answer_outPut()
                user_selection=option
                
                # user_selection1=summary_output_options['find_person']
                
                output = chain.run({
                                        "input_documents": texts,
                                        "output_format" : summary_output_options[user_selection]
                                    })
                st.markdown('**Answer:**.')
                st.text_area(label=":red[Answer]", value=output, height=350,label_visibility="hidden")
    
    
       

        
        
    

if __name__ == "__main__": 
    main()