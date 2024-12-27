import streamlit as st
from display import Presentation

# Set page title and layout
st.set_page_config(
    page_title="CPI-USA",
    layout="wide",
)

st.title("Inflation in the US")
present = Presentation()
present.cpi()
