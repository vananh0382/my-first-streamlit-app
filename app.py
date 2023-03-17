import streamlit as st
import pickle
import sklearn
import numpy as np
model = pickle.load(open("data", "rb"))
st.title("Revenue Prediction")
x_new = st.number_input('Temperature')
x_new = np.array(x_new)
x_new = x_new.reshape(-1,1)
y_new = model.predict(x_new)
if st. button('Predict'):
  st.snow()
	st.write('Revenue Prediction')
	st.success(y_new[0][0])
