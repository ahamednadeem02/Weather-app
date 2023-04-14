import streamlit as st
import plotly.express as px

st.title("Weather forecast app")
place = st.text_input("Place")
days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Select the number of forecasted days you need")

option = st.selectbox("Select data to view", ('Temperature', 'sky'))

st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    dates = ["2022-25-10", "2022-24-2", "2022-23-4"]
    temperatures = [10, 34, 67]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)


figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature"})
st.plotly_chart(figure)