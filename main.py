from langchain_huggingface import HuggingFaceEndpoint
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

token = os.getenv("Your Environment variable")
token = "Paste your HuggingFace Token here"

def LLM(prompt):
    # repo_id = "meta-llama/Meta-Llama-3-8B-Instruct"
    # repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
    repo_id = "microsoft/Phi-3-mini-4k-instruct "
    model = HuggingFaceEndpoint(repo_id=repo_id,huggingfacehub_api_token=token)
    response = model.invoke(prompt)
    return response

# Initializing Frontend part useing streamlit

def main():

    st.title("Chat with Multiple LLM")

    user_questions = st.text_input('Questions...')

    btn = st.button('Ask')

    if btn:
        if user_questions:
            with st.spinner('Generating...'):
                result = LLM(user_questions)
                st.write(result)
        else:
            st.error('ERROR Ask Questions !')
            
if __name__ ==  "__main__":
    main()
