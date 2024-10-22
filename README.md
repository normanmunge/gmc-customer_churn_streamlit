# Predicting Customer Churn for Expresso

Expresso is an African telecommunications company that provides customers with airtime and mobile data bundles. The objective of the [Zindi challenge](https://zindi.africa/competitions/expresso-churn-prediction/) is to develop a machine learning model to predict the likelihood of each Expresso customer “churning,” i.e. becoming inactive and not making any transactions for 90 days.

This solution will help Expresso to better serve their customers by understanding which customers are at risk of leaving.

To access the dataset use this [link](https://drive.google.com/file/d/12_KUHr5NlHO_6bN5SylpkxWc-JvpJNWe/view)


### About the repository

This repository contains 1 [jupyter notebook](https://github.com/normanmunge/gmc-customer_churn_streamlit/blob/main/customer-churn-classification.ipynb) and a [streamlit app](https://github.com/normanmunge/gmc-customer_churn_streamlit/tree/main/streamlit_app) to showcase the predictions on a web interface.

It is a basic app using Streamlit to showcase for my portfolio. Interested parties can fork it and improve on it.

### Running the notebook

The instructions below show how to run the notebooks on a mac terminal.

To run the notebook. Follow the instructions below on a terminal:

#### A. Create a virtual environment

A virtual environment is recommended to install the necessary libraries needed to run the notebook. A virtual environment separates your local projects libraries and the global machine's libraries reducing the chances of conflicts.

`python -m venv [path/to/environments/name-of-env]`

#### B. Activate your virtual environment

`source [path/to/environment]/bin/activate`

#### C. Install necessary libraries

`pip install numpy pandas matplotlib seaborn statsmodels jupyterlab`

#### D. Running the notebook

`jupyter lab`

#### E. Saving and closing your virtual environment

To save your projects, `Cmd + S` will do the trick. Afterwards, on your terminal, enter `deactivate`


