# my-first-streamlit-app
!pip install streamlit
!pip install protobuf==3.20.0
%%writefile app.py
import streamlit as st
st.title("Congratulations!")
st.header("You've just created a website")
st.balloons()
st.snow()
!streamlit run app.py & npx localtunnel --port 8501
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
if st.button('Giải'):
  st.write('Phương trình có 1 nghiệm:', -b/a)
