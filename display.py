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
        "Inflation",
        "Core Inflation",
        "Inflation (percent change)",
        "Core Inflation (percent change)"
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

    # Calculate Purchasing Power for 2023 and 2033
    pp_cpi_2023 = 100 / df.loc["2023-01-01", "CPI"]
    pp_cpi_2033 = 100 / df.loc["2033-01-01", "CPI"]
    
    pp_ccpi_2023 = 100 / df.loc["2023-01-01", "CCPI"]
    pp_ccpi_2033 = 100 / df.loc["2033-01-01", "CCPI"]

    # Calculate Percent Change in Purchasing Power
    pp_cpi_change = ((pp_cpi_2033 - pp_cpi_2023) / pp_cpi_2023) * 100
    pp_ccpi_change = ((pp_ccpi_2033 - pp_ccpi_2023) / pp_ccpi_2023) * 100
    
    if option == "Inflation":
      result = "fig_cpi"
      cpi = mean_cpi.round(3)
      cpi_percent_change = percent_change_cpi.round(3)
      purchasing_power = pp_cpi_2033.round(3)
      purchasing_power_percent_change = pp_cpi_change.round(3)
    elif option == "Inflation (percent change)":
      result = "fig_cpi_pct_chg"
      cpi = mean_cpi.round(3)
      cpi_percent_change = percent_change_cpi.round(3)
      purchasing_power = pp_cpi_2033.round(3)
      purchasing_power_percent_change = pp_cpi_change.round(3)
    elif option == "Core Inflation":
      result = "fig_ccpi"
      cpi = mean_ccpi.round(3)
      cpi_percent_change = percent_change_ccpi.round(3)
      purchasing_power = pp_ccpi_2033.round(3)
      purchasing_power_percent_change = pp_ccpi_change.round(3)
    elif option == "Core Inflation (percent change)":
      result = "fig_ccpi_pct_chg"
      cpi = mean_ccpi.round(3)
      cpi_percent_change = percent_change_ccpi.round(3)
      purchasing_power = pp_ccpi_2033.round(3)
      purchasing_power_percent_change = pp_ccpi_change.round(3)
      
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
    col1.metric("10 Year Avg. CPI (2023-33)", cpi, f"{cpi_percent_change}%", border=True)
    col2.metric("Purchasing Power (2023-33)", purchasing_power, f"{purchasing_power_percent_change}%", border=True)
