import streamlit as st
import requests

st.set_page_config(
    page_title="E-commerce Support Chatbot",
    page_icon="💬"
)

st.title("💬 E-commerce Customer Support Chatbot")
st.write("Ask your question below:")

message = st.text_input(
    "Your message",
    placeholder="Where is my order?"
)

if st.button("Send"):
    if message.strip():

        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={"message": message}
        )

        if response.status_code == 200:
            result = response.json()

            st.success(result["response"])

            st.write("**Language:**", result["language"])
            st.write("**Intent:**", result["intent"])
            st.write("**Route:**", result["route"])

        else:
            st.error("Something went wrong.")