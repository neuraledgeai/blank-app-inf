from business import Model
import streamlit as st
import plotly.express as px

class Presentation:
  
  def __init__(self):
    self.model = Model()

  def cpi(self):
    
    option = st.selectbox(
      "Units/Index:",
      (
        "CPI: All Items in U.S. City Average",
        "Percent Change from Year Ago: CPI: All Items in U.S. City Average",
        "CPI: All Items Less Food and Energy in U.S. City Average",
        "Percent Change from Year Ago: CPI: All Items Less Food and Energy in U.S. City Average"
      ),
    )
    
    if option == "CPI: All Items in U.S. City Average":
      result = "fig_cpi"
    elif option == "Percent Change from Year Ago: CPI: All Items in U.S. City Average":
      result = "fig_cpi_pct_chg"
    elif option == "CPI: All Items Less Food and Energy in U.S. City Average":
      result == "fig_ccpi"
    elif option == "Percent Change from Year Ago: CPI: All Items Less Food and Energy in U.S. City Average":
      result == "fig_ccpi_pct_chg"
      
    fig = self.model.predict(result = result)
    
    # Improve the layout and design
    fig.update_layout(
        dragmode=False,
        title_font=dict(size=20, family="Arial"),
        xaxis=dict(
            showgrid=True, 
            gridcolor="lightgrey",
            rangeslider=dict(visible=True, bgcolor="#636EFA", thickness=0.05),  
        ),
        yaxis=dict(showgrid=True, gridcolor="lightgrey"),
    )
    
    st.plotly_chart(fig)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("CPI 2023", "304.701", "204.701%")
    col2.metric("10 Year Avg. CPI (2023-33)", "462.196", "51.688%")
    col3.metric("3 Year Avg. CPI (2023-26)", "383.496", "25.859%")
    col4.metric("CPI 2025", "383.126", "25.738%")
