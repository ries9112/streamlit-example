import streamlit as st
import numpy as np
import pandas as pd
import pins
import plotly.express as px

# Pull data
@st.cache
def load_data():
    df = pins.pin_get("hitBTC_orderbook", board = "https://raw.githubusercontent.com/predictcrypto/pins/master/")
    return df
# Pull data
df = load_data()

# Sidebar user input
crypto_symbol = st.sidebar.selectbox(
    'Which cryptocurrency do you want to visualize?',
     df['symbol'])
# Show the data
st.write("Preview of the latest data (all cryptocurrencies):")
# Move date time to the front
df = df[ ['date_time_utc'] + [ col for col in df.columns if col != 'date_time_utc' ] ]
# Arrange by date time
df.sort_values(by=['date_time_utc'])
# Show data
st.write(df.head(250))

# Show selected cryptocurrency
'Data for the ', crypto_symbol, 'cryptocurrency:'
# Display data
st.write(df[(df.symbol == crypto_symbol)])
# Add note about changing selection
st.write('Use the sidebar on the left to change the selected cryptocurrency')

# Plot the data
state_total_graph = px.line(
        df[(df.symbol == crypto_symbol)], 
        x='date_time_utc',
        y='ask_1_price')

st.plotly_chart(state_total_graph)
