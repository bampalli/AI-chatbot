import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image

import os
os.environ['GEMINI_API_KEY'] = 'AIzaSyAF1Cg0d5FDc4rIVmB_I9XiIKeClYFVRjY'

import google.generativeai as genai
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

## Function to load google model and get respones

def get_gemini_response(input,text):
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    if input!="":
       response = model.generate_content([input,text])
    else:
       response = model.generate_content(text)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title=" AI CHATBOT App")

st.header("RAHUL AI CHATBOT APP")
input=st.text_input("Input Prompt: ",key="input")


submit=st.button("click here for response")

## If ask button is clicked

if submit:
   
    response=get_gemini_response(input,"text")
    st.subheader("The Response is")
    st.write(response)