import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title='Country',
    page_icon='🇧🇷',
    layout='wide',
    initial_sidebar_state='expanded'
)


df = st.session_state['data']
all_countries = df['NOC'].unique()

slider = st.slider('Select time range',
                   min_value=df['Year'].min(),
                   max_value=df['Year'].max(),
                   value=(df['Year'].min(), df['Year'].max()),
                   step=1)

filtered_df = df[(df['Year'] >= slider[0]) & (df['Year'] <= slider[1])]
st.write(f"Showing data from {slider[0]} to {slider[1]}")

country_filter = st.multiselect('Choose a country',
                                options=all_countries,
                                default=['USA', 'RUS', 'BRA', 'GER'])

filtered_df = filtered_df[filtered_df['NOC'].isin(country_filter)]

medals_by_country = filtered_df.groupby(['NOC'])['Medal'].count().reset_index()
medals_by_country = medals_by_country.sort_values(by='Medal', ascending=False)

fig = px.bar(medals_by_country,
             x='NOC',
             y='Medal',
             text='Medal',
             labels={'NOC': 'Country', 'Medal': 'Number of Medals'},
             color='Medal',
             title='Number of Medals by Country')

st.plotly_chart(fig, use_container_width=True)

st.sidebar.markdown('Developed by [André](https://github.com/nine913)')