#import requests
#import pandas as pd
#import geopandas as gpd

from datetime import datetime
from pathlib import  Path


#user Input section :

def get_start_end_dates():

    start_date=input("ENTER THE STARTING DATE HERE: in YYYY-MM-DD format (e.g. 2023-01-01): ")
    print(f"Starting Date from:{start_date}")
    end_date=input("ENTER THE ENDING DATE HERE: in YYYY-MM-DD format (e.g. 2023-01-31): ")

    magnitude=input("ENTER MAGNITUDE: in decimal format (e.g. 5.0): ")

    return start_date, end_date, magnitude
print(get_start_end_dates()) 

def request_data(start_date,end_date,magnitude):
    url=None
    response=requests.get(url)
    data=response.json()

    return data
def save_data(data):
    