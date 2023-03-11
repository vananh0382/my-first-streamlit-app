import streamlit as st
st.title("Giải phương trình bậc nhất")
st.balloons()
st.snow()
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
if st.button('Giải'):
  if a == b == 0:
    st.write('Phương trình có vô số nghiệm')
  elif a == 0 and b != 0:
    st.write('Phương trình vô nghiệm')
  else:
    st.write('Phương trình có 1 nghiệm:', -b/a)
