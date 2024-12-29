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


st.info("Notes")
content = """
<div style="text-align: justify; font-size: 12px;">
    <p>The Consumer Price Index for All Urban Consumers: All Items is a price index of a basket of goods and services paid by urban consumers in the United States. 
    It is compiled by the U.S. Bureau of Labor Statistics and measures changes in the price level of this basket over time. The index is used to assess price changes associated 
    with the cost of living and is a key indicator of inflation. The data reflects the spending patterns of urban consumers, which represent approximately 93% of 
    the total U.S. population.</p>
    <p>The Consumer Price Index for All Urban Consumers: All Items Less Food and Energy is a price index that measures the changes in the cost of a basket of goods 
    and services, excluding the volatile food and energy sectors. This index is also compiled by the U.S. Bureau of Labor Statistics and is used to provide a clearer view of 
    the underlying inflation trends by excluding the often fluctuating prices of food and energy.</p>
    <p>The model used for predictions is trained on historical data from 1960 up to 2023. Therefore, the predictions generated by the model start from the year 2024 onwards. It 
    is important to note that the model may make mistakes, and individual predictions might not always be accurate. However, the reliability of the model's predictions can be 
    assessed based on their average accuracy over time.</p>
</div>
"""

# Render the HTML content in Streamlit
st.markdown(content, unsafe_allow_html=True)
