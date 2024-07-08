import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import pickle

model=pickle.load(open("lr.pkl","rb"))

#Streamllit UI for user Input
st.title("House Price Prediction")

SquareFeet=st.number_input("Enter the size of the house",min_value=1000,max_value=2999,step=50)
Bedrooms=st.number_input("Enter the number of Bedrooms",min_value=2,max_value=5,step=1)
Bathrooms=st.number_input("Enter the number of Bathrooms",min_value=1,max_value=3,step=1)
Neighborhood=st.radio("Enter the neighborhood",['Rural','Urban','Suburban'])
neighbor=1 if Neighborhood=="Rural" else 2 if Neighborhood=="Urban" else 3
YearBuilt=st.number_input("Enter the Year of Construction",min_value=1950,max_value=2021,step=1)

#Preprocess Input Data
input_data = np.array([[SquareFeet, Bedrooms, Bathrooms, neighbor, YearBuilt]])

#Predict House Price
if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.write(f"The predicted price of the house is: {prediction[0]:,.2f}")
