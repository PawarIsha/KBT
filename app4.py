import streamlit as st
st.title("simple chatbot")
Question=st.text_input("Ask me anything")
if st.button("send"):
    st.write("You asked",Question)
    st.write("chatbot is on process  i will reply soon")