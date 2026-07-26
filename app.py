import streamlit as st
from rag_pipeline import ask_question

st.set_page_config(page_title="Insurance Claims AI Assistant")

st.title("🏥 Insurance Claims AI Assistant")

question = st.text_input("Ask a question")

if st.button("Submit"):

    if question:

        answer = ask_question(question)

        st.write("### Answer")

        st.write(answer)