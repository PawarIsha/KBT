import streamlit as st
st.markdown("""
<style> 
            stApp{
                background-color:white!important;
            }
            .stButton > button
            {
                background-color:"green" !important;
                color:"white" !important;
                border-radius:50% !important;
            }

</style>




""",unsafe_allow_html=True)
st.title("Welcome to basic streamliy app")

age = st.slider("Select ur age", 1 , 100)

city = st.selectbox("Select ur city", ["Delhi","Mumbai","Nashik","Pune"])

if st.button("Show the details"):
    st.write("Age:",age)
    st.write("City:",city)