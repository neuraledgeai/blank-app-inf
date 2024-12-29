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
    df = self.model.predict(result="dataframe")
    # Filter for predicted values (2024–2033)
    df_predicted = df[df["Label"] == "Predicted"]
    
    # Calculate the mean CPI and CCPI for the predicted values
    mean_cpi = df_predicted["CPI"].mean()
    mean_ccpi = df_predicted["CCPI"].mean()
    
    # Get the actual CPI and CCPI values for 2023
    actual_cpi_2023 = df.loc["2023-01-01", "CPI"]
    actual_ccpi_2023 = df.loc["2023-01-01", "CCPI"]
    
    # Calculate percent change from 2023 actual to predicted mean
    percent_change_cpi = ((mean_cpi - actual_cpi_2023) / actual_cpi_2023) * 100
    percent_change_ccpi = ((mean_ccpi - actual_ccpi_2023) / actual_ccpi_2023) * 100
    
    if option == "CPI: All Items in U.S. City Average":
      result = "fig_cpi"
      cpi = mean_cpi
      percent_change = percent_change_cpi
    elif option == "Percent Change from Year Ago: CPI: All Items in U.S. City Average":
      result = "fig_cpi_pct_chg"
      cpi = mean_cpi
      percent_change = percent_change_cpi
    elif option == "CPI: All Items Less Food and Energy in U.S. City Average":
      result = "fig_ccpi"
      cpi = mean_ccpi
      percent_change = percent_change_ccpi
    elif option == "Percent Change from Year Ago: CPI: All Items Less Food and Energy in U.S. City Average":
      result = "fig_ccpi_pct_chg"
      cpi = mean_ccpi
      percent_change = percent_change_ccpi
      
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
    
    col1, col2 = st.columns(2)
    col1.metric("CPI", cpi, percent_change)
    col2.metric("10 Year Avg. CPI (2023-33)", "462.196", "51.688%")
