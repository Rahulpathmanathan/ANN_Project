import streamlit as st
import pickle
import pandas as pd
import numpy as np
import tensorflow as tf
import sklearn
from tensorflow.keras.models import Sequential  
from tensorflow.keras.layers import Dense

def dlmodel(input):
    loaded_model= pickle.load(open("model.pkl","rb"))
    result= loaded_model.predict(input)
    rounded_prediction = np.round(result).astype(int)
    if rounded_prediction[0] ==1:
        return "Customer has been churned, Please do provide dicounts and try to retain"
    else:
        return "Customer is still in business"  

st.markdown("<div style='text-align: center;'><h1>Retention Analysis</h1></div>", unsafe_allow_html=True)

with st.form("my_form"):

    st.markdown("<div style='text-align:center;'><h3>Please fill the Below Details to Predict</h3></div>", unsafe_allow_html=True)
   
    st.write("")
    col1, col2, col3 = st.columns(3)

    with col1:
        v1 = st.number_input("please enter Average time between orders:", min_value=1, max_value=1000)
        

    with col2:    
        v3 = st.slider("Total Order Count:", min_value=0, max_value=50)
        v4 = st.slider("Cancelled / Returned Order Count:", min_value=0, max_value=50)
        submitted = st.form_submit_button("Predict") 
        
    with col3:
        v2 = st.number_input("Days Since Last Order:", min_value=1, max_value=1000)

if submitted:
    input=np.array([[v1,v2,v3,v4]])
    prediction = dlmodel(input)
    st.write(prediction)
                    