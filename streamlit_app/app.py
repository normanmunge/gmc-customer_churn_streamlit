import streamlit as st
from dotenv import load_dotenv
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.linear_model import LogisticRegression
import random

#Load environment variables
load_dotenv()

# load the data
def load_data():
    return pd.read_csv('../datasets/Espresso_churn_clean_dataset.csv')


# Handling outliers using the IQR method
def outlier_limits(col):
    Q3, Q1 = np.nanpercentile(col, [75,25])
    inter_quartile_range = Q3 - Q1
    upper_limit = Q3 + (1.5*inter_quartile_range)
    lower_limit = Q1 - (1.5*inter_quartile_range)
    return upper_limit, lower_limit

def handle_outliers(df):
    outlier_cols = df.drop(df.select_dtypes(include=['object']).columns.tolist(), axis=1)
    outlier_cols.drop('churn', axis=1, inplace=True) #Let's drop churn since it will be our target column
    outlier_cols.columns.tolist()

    for col in outlier_cols:
        UL, LL = outlier_limits(df[col])
        df.loc[(df[col] > UL), col] = UL
        df.loc[(df[col] < LL), col] = LL

    return df

# Encoding our dataset
def encode_data(df):
    encoder = LabelEncoder()

    for col in df.columns:
        # Encoding only object data types and excluding the region_name column since we want to display it on the app
        if df[col].dtype == 'object' and col != 'region_name':
            df[col] = encoder.fit_transform(df[col])

    return df

# Model Training
def train_model(df):
    X = df[['region', 'num_of_connections', 'zone1_calls', 'zone2_calls', 'regularity', 'active_pack']]
    y = df['churn']

    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Training the model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Making predictions
    y_pred = model.predict(X_test)

    # Return the model, X_test and y_pred variables
    return model, X_test, y_pred
    #prediction_proba = model.predict_proba(X_test)


def evaluate_model(model, test_data):
    prediction_proba = model.predict_proba(test_data)
    return pd.DataFrame(prediction_proba).rename(columns={
        0: 'Actual',
        1: 'Predicted'
    })


def preprocess_data(df):
    # Renaming our columns for easier reference
    df.rename(inplace=True, columns={
        "TENURE": "network_duration",
        "MONTANT": "topup_amount",
        "FREQUENCE_RECH": "num_refill_amount",
        "REVENUE": "monthly_income",
        "ARPU_SEGMENT": "income_over_90days_3",
        "FREQUENCE": "num_times_income_generated",
        "DATA_VOLUME": "num_of_connections",
        "ON_NET": "inter_espresso_call",
        "ORANGE": "orange_calls",
        "TIGO": "tigo_calls",
        "ZONE1": "zone1_calls",
        "ZONE2": "zone2_calls",
        "MRG": "visiting_client",
        "TOP_PACK": "active_pack",
        "FREQ_TOP_PACK":"frequency_activating_top_pack"
    })

    # Converting to lower case and replacing spaces with underscores
    df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

    df['region_name'] = df['region']
    df['active_pack_description'] = df['active_pack']

    with st.expander('Data'):
        st.write(df.head())

    # Handling outliers in our dataset
    df = handle_outliers(df)

    # Encoding the dataset
    df = encode_data(df)

    model, X_test, y_pred = train_model(df)

    return evaluate_model(model, X_test)


def define_input_handlers(df, features):
    #features_ = [f'{col.capitalize().replace("_", " ")}' for col in features]
                
    #categorical_features = ['region_name', 'active_pack_description']

    #slider_features = [col for col in features_ if col not in categorical_features]

    for feature in features:
        unique_values = df[feature].unique().tolist()
        st.selectbox(feature, unique_values)
        # Set dropdowns for categorical columns
        # if ['region_name', 'active_pack_description'] in features:
        #     feature_name = f'{feature.capitalize().replace("_", " ")}'
        #     unique_values = df[feature].unique().tolist()
        #     st.selectbox(feature_name, unique_values)
        # else:
        # Set the slider for numerical columns
        # feature_name = f'{feature.capitalize().replace("_", " ")}'
        # st.slider(feature_name, df[feature].min(), df[feature].max(), df[feature].mean())
        

def main():
    st.set_page_config(
        page_title = 'Customer Churn Prediction',
        layout = 'centered'
    )

    st.title('Predict customer churn')

    st.info('This is a simple demo of how to build a customer churn prediction app using Streamlit.')

    df = load_data()

    prediction_prob = preprocess_data(df)

    prediction_prob

    with st.sidebar:
        st.header('Input features')

        st.write('Add parameters to see the prediction')

        features = ['region_name','active_pack_description', 'num_of_connections', 'zone1_calls', 'zone2_calls', 'regularity']
        target = 'churn'

        #unique_values = define_input_handlers(df, features)


main()

        
        


    # features = ['region', 'num_of_connections', 'zone1_calls', 'zone2_calls', 'regularity', 'active_pack']
    # target = 'churn'

    # st.write(df.head())

    # model, predictions = preprocess_data(df)

    # st.header('Input Fields')

    



# features = ['region', 'num_of_connections', 'zone1_calls', 'zone2_calls', 'regularity', 'active_pack']
# target = 'churn'

#print(df.head())


# with st.expander('Data'):
#     st.write('This dataset contains the following columns:')
#     df = pd.read_csv('../datasets/Expresso_churn_dataset.csv')
#     df.rename(inplace=True, columns={
#         "TENURE": "network_duration",
#         "MONTANT": "topup_amount",
#         "FREQUENCE_RECH": "num_refill_amount",
#         "REVENUE": "monthly_income",
#         "ARPU_SEGMENT": "income_over_90days_3",
#         "FREQUENCE": "num_times_income_generated",
#         "DATA_VOLUME": "num_of_connections",
#         "ON_NET": "inter_espresso_call",
#         "ORANGE": "orange_calls",
#         "TIGO": "tigo_calls",
#         "ZONE1": "zone1_calls",
#         "ZONE2": "zone2_calls",
#         "MRG": "visiting_client",
#         "TOP_PACK": "active_pack",
#         "FREQ_TOP_PACK":"frequency_activating_top_pack"
#     })


