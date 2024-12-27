import pandas as pd

class LocalDatabase:
  def __init__(self, cpi_dataset="CPI_for_urban_consumers_all_items_US_city_average.csv", m2_dataset="M2.csv"):
    self.cpi = pd.read_csv(cpi_dataset)
    self.m2 = pd.read_csv(m2_dataset)

  def load_data(self):
    
    # Convert 'observation_date 'to datetime and assign to 'Date'
    self.cpi["Date"] = pd.to_datetime(cpi["observation_date"]) 
    self.m2["Date"] = pd.to_datetime(m2["observation_date"])

    # Drop the 'observation_date' column
    self.cpi.drop(columns=["observation_date"], inplace=True)
    self.m2.drop(columns=["observation_date"], inplace=True)

    # Rename columns
    self.cpi.rename(columns={"CPIAUCSL": "CPI"}, inplace=True)
    self.m2.rename(columns={"M2SL": "M2"}, inplace=True)
    
    # Set 'Date' as the index for both dataframes
    self.cpi.set_index('Date', inplace=True)
    self.m2.set_index('Date', inplace=True)
    
    # Concatenate the two DataFrames along the columns
    df = pd.concat([self.cpi, self.m2], axis=1)

    return df

    
