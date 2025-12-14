# streamlit_app.py
import streamlit as st
from core.coder import vibe_coder

st.set_page_config(page_title="Vibe Coder", layout="wide")
st.title("🧠 Personal Vibe Coder")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

user_input = st.chat_input("Describe what you want to build...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        response = vibe_coder(
            user_input,
            st.session_state.messages
        )
        st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
