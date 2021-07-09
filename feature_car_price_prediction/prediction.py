import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import os
import streamlit as st

def run_it():

    st.title('Car Price Prediction')

    # cwd = os.getcwd()  # Get the current working directory (cwd)
    # files = os.listdir(cwd)  # Get all the files in that directory
    # print("Files in %r: %s" % (cwd, files))

    model = pickle.load(open('feature_car_price_prediction/random_forest_regression_model.pkl', 'rb'))
    standard_to = StandardScaler()

    Present_Price = 7.60
    Kms_Driven2 = np.log(77632)
    Owner = 0
    Year = 6
    Fuel_Type_Diesel = 1
    Fuel_Type_Petrol = 0
    Seller_Type_Individual = 0
    Transmission_Mannual = 1
    
    prediction=model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
    output=round(prediction[0],2)
    st.write(f"You Can Sell The Car at {output}K") #st.write("You Can Sell The Car at {}K".format(output))
