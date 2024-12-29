import streamlit as st
from display import Presentation

# Set page title and layout
st.set_page_config(
    page_title="CPI Machine",
    layout="wide",
)

present = Presentation()

st.title("Consumer Price Index in the USA")
present.cpi()



content = """
<div style="text-align: justify; font-size: 12px;">
    <p>This is a sample text that is justified from the left end to the right end with a smaller font size.</p>
    <p>You can write your content here and it will be displayed in a justified manner.</p>
</div>
"""

# Render the HTML content in Streamlit
st.markdown(content, unsafe_allow_html=True)
