import joblib
import pandas as pd
from database import LocalDatabase
import plotly.express as px

class Model:
  def __init__(self, cpi_model="cpi_model.pkl", m2_model="m2_model.pkl"):
    self.cpi_model = joblib.load("cpi_model.pkl")
    self.m2_model = joblib.load("m2_model.pkl")
    self.db = LocalDatabase()

  def predict(self, years = range(1,10), result="fig_cpi"):
    # Load training data from database
    df = self.db.load_data()
    
    # Initialize M2 value and corresponding year
    m2 = 20810.3  # M2 for 2023
    corresponding_year = 2023
    
    # Lists to store predicted M2s and corresponding years
    predicted_m2s = []
    corresponding_years = []
    
    for year in years:
        # Prepare the data for prediction
        #X = np.array([[m2]])
        X = pd.DataFrame({"M2_L1": [m2]})
    
        # Make prediction using the trained model
        predicted_m2 = self.m2_model.predict(X)
    
        # Update M2 and corresponding year for the next iteration
        m2 = predicted_m2[0]  # Update the value of m2 for the next year
        corresponding_year += 1
    
        # Append the results to the respective lists
        predicted_m2s.append(predicted_m2[0])  # Store as a scalar
        corresponding_years.append(corresponding_year)

    # Create a DataFrame to store forecasted results
    df_predicted_m2 = pd.DataFrame({
      "Year": corresponding_years,
      "M2": predicted_m2s
    })
    
    # Convert Year to pandas datetime and set as index
    df_predicted_m2["Year"] = pd.to_datetime(df_predicted_m2["Year"], format="%Y")
    df_predicted_m2.set_index("Year", inplace=True)
    
    # Predict CPI
    predicted_cpis = self.cpi_model.predict(df_predicted_m2)  
    
    # Create a DataFrame with the predicted CPI values and the corresponding datetime index
    df_predicted_cpi = pd.DataFrame(
        predicted_cpis, 
        columns=["CPI"],  # Name of the column with predictions
        index=df_predicted_m2.index  # Use the same datetime index from df_predicted_m2
    )
    
    # Concatenate actual and predicted M2 DataFrames
    df_cpi = pd.concat([df, df_predicted_cpi])
    df_cpi = df_cpi.drop(columns=["M2"])
    
    # Percent Change Year Ago for CPI
    df_cpi["pct_chg"] = df_cpi["CPI"].pct_change() * 100
    df_cpi = df_cpi.dropna()
    
    # Figure for CPI
    fig_cpi = px.line(
        df_cpi,
        y="CPI",
        title=(
            "Consumer Price Index for All Urban Consumers: "
            "All Items in U.S. City Average (1961 - 2032)"
        ),
        labels={
            "CPI": "CPI (Index 1982-1984=100)",
            "index": "Year"
        },
        template="plotly_white"
    )
    
    # Figure for CPI percent change
    fig_pct = px.line(
        df_cpi,
        y="pct_chg",
        title="Percentage Change a Year Ago in CPI",
        labels={"pct_chg": "% Change a Year Ago", "index": "Year"},
        template="plotly_white"
    )
    
    return fig_pct if result == "fig_cpi_pct_chg" else fig_cpi
