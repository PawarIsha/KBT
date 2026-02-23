import streamlit as st
st.title("Basic claculator")
num1=st.number_input("Enter your first number",step =1)
num2=st.number_input("Enter your second number",step =1)
Operation=st.selectbox("choose op",["add","sub","mul","div"])
if st.button("Calculate"):
    if Operation == "add":
        st.write(num1+num2)
    elif Operation == "sub":
        st.write(num1-num2)
    elif Operation == "mul":
        st.write(num1*num2)
    elif Operation == "div":
        if num2!=0:
            result=num1/num2
        else:
            result="cannot divide by zero"
    st.write("The result is",result)
