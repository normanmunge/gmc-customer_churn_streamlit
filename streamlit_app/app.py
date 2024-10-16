import streamlit as st
import os
import time
from dotenv import load_dotenv
import pandas as pd

#Load environment variables
load_dotenv()

st.set_page_config(
    page_title = 'Customer Churn Prediction',
    layout = 'centered'
)

st.title('Predict customer churn')

st.write('This is a simple demo of how to build a customer churn prediction app using Streamlit.')

st.header('Input Fields')

df = pd.read_csv('https://drive.google.com/file/d/12_KUHr5NlHO_6bN5SylpkxWc-JvpJNWe/view/VariableDefinitions.csv')

features = ['region', 'num_of_connections', 'zone1_calls', 'zone2_calls', 'regularity', 'active_pack']

df.head()

for feature in features:
    unique_values = df[feature].unique().tolist()
    print(unique_values)
    st.write(unique_values)
    st.selectbox(f'{feature}', unique_values)
