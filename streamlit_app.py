import streamlit as st
from database import LocalDatabase

st.title("🎈 My new app hi")
db = LocalDatabase()
df = db.load_data()
st.dataframe(df)
