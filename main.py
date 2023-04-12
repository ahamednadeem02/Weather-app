import streamlit as st

st.title("Weather forecast app")
place = st.text_input("Place")
days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Select the number of forecasted days you need")

option = st.selectbox("Select data to view", ('Temperature', 'sky'))

st.subheader(f"{option} for the next {days} days in {place}")