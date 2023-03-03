# my-first-streamlit-app
import streamlit as st
st.title("Giải phương trình bậc nhất")
st.balloons()
st.snow()
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
if st.button('Giải'):
  st.write('Phương trình có 1 nghiệm:', -b/a)
import streamlit as st
