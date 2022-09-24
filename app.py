import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import preprocessing
import tweepy

df = pd.read_excel("fo_mktlots.xlsx")

ek_ghanta = preprocessing.pichla_ek_ghanta(df)

st.sidebar.title("Twitter-Sentiment-Analysis")

time = 'Last Hour count'

if(time == 'Last Hour count'):
    st.header("Previous Hour count")
    st.bar_chart(data = ek_ghanta, x = 'keyword' ,y = 'count')