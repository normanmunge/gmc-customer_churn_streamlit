import streamlit as st
import os
import time
from dotenv import load_dotenv

#Load environment variables
load_dotenv()

st.set_page_config(
    page_title = 'Customer Churn Prediction',
    layout = 'centered'
)

st.title('Predict customer churn')