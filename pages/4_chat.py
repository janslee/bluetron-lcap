from openai import OpenAI

client = OpenAI(api_key="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")
import streamlit as st
from streamlit_chat import message


if 'conversation' not in st.session_state:
    st.session_state.conversation = []

def chat_with_bot(message):
    st.session_state.conversation.append({"role": "user", "content": message})
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=st.session_state.conversation)
    assistant_response = response.choices[0].message.content
    st.session_state.conversation.append({"role": "assistant", "content": assistant_response})

st.title("OpenAI Streamlit 聊天机器人")

def get_text():
    input_text = st.text_input("You:", "Hello, how are you?", key="input")
    return input_text

user_input = get_text()
send_button = st.button("Send")

if send_button and user_input:
    chat_with_bot(user_input)

if st.session_state.conversation:
    for i, msg in enumerate(st.session_state.conversation):
        if msg['role'] == 'user':
            message(msg['content'], is_user=True, key=str(i))
        else:
            message(msg['content'], key=str(i))