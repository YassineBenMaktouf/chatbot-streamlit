import openai
from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
client = OpenAI()


st.title(":speech_balloon: Chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    openai.api_key =  os.getenv("OPENAI_API_KEY")
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(
    messages=[{
        "role": "user",
        "content": prompt,
    }],
    model="gpt-3.5-turbo",
)
    
    # Check if the response has any choices
    if response.choices:
        # Access the message content directly as an attribute
        assistant_response = response.choices[0].message.content

        # Append this response to the conversation history in Streamlit
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        st.chat_message("assistant").write(assistant_response)