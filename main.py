import pandas as pd

import streamlit as st

import plotly.express as px

from flask import Flask

app = Flask(__name__)

st.title('Credit Card Fraud Detection ')


@st.cache
def load_data(nrows):
    data = pd.read_csv('fraudTrain.csv', nrows=nrows)
    return data


data_load_state = st.text('Loading data ....')
weekly_data = load_data(10)

st.subheader('DataSet credit card')
st.write(weekly_data)

st.subheader('Bar Chart')
bar_chart = px.bar(weekly_data, x="merchant", y="amt", color_discrete_sequence=['#F63366'] * len(weekly_data),
                   template='plotly_white')
st.plotly_chart(bar_chart)

st.subheader('Line Chart')
line_chart = px.line(weekly_data, x="merchant", y="amt", color_discrete_sequence=['#F63366'] * len(weekly_data),
                     template='plotly_white')
st.plotly_chart(line_chart)
