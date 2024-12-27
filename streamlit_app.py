import streamlit as st
from business import Model

st.title("🎈 My new app hiee")
model = Model()
fig = model.predict()
st.plotly_chart(fig)
