from business import Model
import streamlit as st
import plotly.express as px

class Presentation:
  
  def __init__(self):
    self.model = Model()

  def cpi(self):
    option = st.selectbox(
      "Units:",
      ("Index 1982-1984=100", "Percent Change from Year Ago"),
    )
    
    if option == "Index 1982-1984=100":
      result = "fig_cpi"
    elif option == "Percent Change from Year Ago":
      result = "fig_cpi_pct_chg"
      
    fig = self.model.predict(result = result)
    fig.update_layout(
        dragmode=False,
        showlegend=True
    )
    st.plotly_chart(fig)
    
