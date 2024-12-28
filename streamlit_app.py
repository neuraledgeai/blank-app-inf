import streamlit as st
from display import Presentation

# Set page title and layout
st.set_page_config(
    page_title="CPI Machine",
    layout="wide",
)

st.title("CPI MACHINE")
st.subheader("Consumer Price Index in the US")
present = Presentation()
present.cpi()
