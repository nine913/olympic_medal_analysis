import streamlit as st

st.set_page_config(
    page_title='Atheletes',
    page_icon='🥇',
    layout='wide',
    initial_sidebar_state='expanded'
)

df = st.session_state['data']

df['Decade'] = (df['Year'] // 10) * 10
decade_filter = st.selectbox("Choose a decade", sorted(df['Decade'].unique()))
filtered_df = df[df['Decade'] == decade_filter]

athletes = filtered_df['Name'].unique()
athlete_filter = st.selectbox("Choose an athlete", athletes)
filtered_df = filtered_df[filtered_df['Name'] == athlete_filter]

athlete_data = filtered_df.iloc[0]

st.markdown(f"""
### 🏅 {athlete_data['Name']}
- **Sex:** {athlete_data['Sex']}
- **Age:** {athlete_data['Age']}
- **Height:** {athlete_data['Height']} cm
- **Weight:** {athlete_data['Weight']} kg
- **Team:** {athlete_data['Team']}
- **Sport:** {athlete_data['Sport']}
- **Total participations:** {len(filtered_df)}
""")

st.dataframe(filtered_df[['Year', 'Event', 'Medal']].sort_values('Year'))

st.sidebar.markdown('Developed by [André](https://github.com/nine913)')