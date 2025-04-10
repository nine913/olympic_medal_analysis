import pandas as pd
import webbrowser
import streamlit as st


if 'data' not in st.session_state:
    df = pd.read_csv('Clean_olympics.csv')
    st.session_state['data'] = df

st.set_page_config(
    page_title='Home',
    page_icon='🏠',
    layout='wide',
    initial_sidebar_state='expanded'
)

st.markdown("""
# Olympic Games Data Analysis🥇
""")
st.sidebar.markdown('Developed by [André](https://github.com/nine913)')


button = st.button('Access data on Kaggle')


if button:
    webbrowser.open('https://www.kaggle.com/code/narminhumbatli/120-years-of-olympic-history-athletes-and-results/input')


st.markdown("""A dataset with historical records from 120 years of the Olympics, where I filtered only those who won medals over those years.""")
