"""Get data from API."""

from datetime import datetime
import numpy as np
import pandas as pd
import requests

from sql_commands import SQL_DB, SQL_TABLE
from sqlite_cli import SqLiteClient
from api_key import key

api_key  = key

## request data from FRED api, GDP series
url = f"https://api.stlouisfed.org/fred/series/observations?series_id=GDP&api_key={api_key}&file_type=json"

response = requests.get(url)

df = pd.DataFrame(response.json()['observations'])  # convert to dataframe
df = df[['date', 'value']]  # select columns



BASE_URL = 'https://api.stlouisfed.org/fred/series'
API_KEY = key



def _get_series_data(series_id):
    current_datetime = datetime.now().strftime("%Y-%m-%d")
    end_point = (
        f"{BASE_URL}/observations?series_id={series_id}"
        f"&api_key={API_KEY}&file_type=json"
    )
    print(f"Getting data from {end_point}...")
    response = requests.get(end_point)
    df = pd.DataFrame(response.json()['observations'])  # convert to dataframe
    df = df.drop([0,1,2,3])
    df['pct_change'] = df.value.astype(float).pct_change()
    df = df[['date', 'value', 'pct_change']]  # select columns



    df.to_csv(f"dataset\\{current_datetime}_gdp.csv")
     

def _insert_data():
    current_datetime = datetime.now().strftime("%Y-%m-%d")
    df = pd.read_csv(f"dataset\\{current_datetime}_gdp.csv")
    sql_cli = SqLiteClient(SQL_DB)
    sql_cli.insert_from_frame(df, SQL_TABLE)
    
    return
    
if __name__ == '__main__':
    df = _get_series_data('GDP')
    print(df)