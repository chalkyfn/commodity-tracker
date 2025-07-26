import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts
import plotly.express as px
import pandas as pd 
import requests
import time



API_URL = "http://127.0.0.1:8000/prices"

st.title("Real Time Commodity Price Tracker")

auto_refresh = st.checkbox("Auto-refresh every 5 seconds", value=True)

chart_container = st.empty()
table_container = st.empty()

price_history = []

while True:
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()["prices"]
        df = pd.DataFrame(data)
        df["Time"] = pd.Timestamp.now()

        price_history.append(df)

        history_df = pd.concat(price_history)

        table_container.dataframe(df[["name", "price"]])

         # Plot line chart for each commodity
        fig = px.line(
            history_df,
            x="Time",
            y="price",
            color="name",
            title="Price Trend Over Time"
        )
        chart_container.plotly_chart(fig, use_container_width=True)

    else:
        st.error(f"Failed to fetch data. Status: {response.status_code}")

    if not auto_refresh:
        break

    time.sleep(5)
