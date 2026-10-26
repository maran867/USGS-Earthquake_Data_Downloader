#import requests
#import pandas as pd
#import geopandas as gpd

from datetime import datetime
from pathlib import  Path


#user Input section :

start_date=input("ENTER THE STARTING DATE HERE: in YYYY-MM-DD format (e.g. 2023-01-01): ")

end_date=input("ENTER THE ENDING DATE HERE: in YYYY-MM-DD format (e.g. 2023-01-31): ")

magnitude=input("ENTER MAGNITUDE: in decimal format (e.g. 5.0): ")