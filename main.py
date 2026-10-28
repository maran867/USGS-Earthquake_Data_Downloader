import requests
import pandas as pd
import geopandas as gpd
import folium

from datetime import date
from pathlib import Path

#STEP 1 : USER INPUT SECTION

def get_start_end_dates():
    #getting user input for the start date and end date and magnitude.
    while True: 
       start_date_str = input("ENTER THE STARTING DATE HERE: in YYYY-MM-DD format (e.g. 2023-01-01): ")
       try:
           #checking the input date is in correct format or not
           start_date = date.fromisoformat(start_date_str)
           break
       except ValueError:
           print(f"{start_date_str} Entered date format is not correct. Please try again.")
           
    while True:  
        end_date_str = input("ENTER THE ENDING DATE HERE: in YYYY-MM-DD format (e.g. 2023-01-31): ")
        try:
            end_date = date.fromisoformat(end_date_str)
            if end_date <= start_date:
                print("End date cannot be earlier than start date. Please enter a valid end date.")
            else:
                break
        except ValueError:
            print(f"{end_date_str} Entered date format is not correct. Please try again.")
            
    while True:
        try:
            magnitude_str = input("ENTER MAGNITUDE: in decimal format (e.g. 5.0): ")
            magnitude = float(magnitude_str)
            break
        except ValueError:
            print(f"{magnitude_str} Entered magnitude format is not correct. Please try again.")
            
    return start_date, end_date, magnitude


#REQUESTING DATA FROM USGS API

def request_data(start_date, end_date, magnitude):
    url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&orderby=magnitude-asc&starttime={start_date}&endtime={end_date}&minmagnitude={magnitude}"
    response = requests.get(url, timeout=10)
    data = response.json()
    print("Earthquakes returned:", data["metadata"]["count"])
    return data


#CHANGING THE JSON FORTMAT TO GEODATAFRAME FORMAT

def format_change(data):
  # Direct, robust way to convert USGS GeoJSON format into a GeoDataFrame
  gdf = gpd.GeoDataFrame.from_features(data["features"], crs="EPSG:4326")
  print(f"Stuctures of the GeodataFrame : {gdf.head(5)}")
  output_as_csv=None
  output_as_GeoJSON=None
  return gdf



#VISUALIZING THE DATA IN FOLIUM MAP
def visualize_data(gdf):
    # Center using mean Latitude (y) and Longitude (x)
    m=folium.Map(location=[gdf.geometry.y.mean(),gdf.geometry.x.mean()],
                 zoom_start=2,tiles="Esri.WorldImagery",attr="Esri,USGS")
                 
    for _, row in gdf.iterrows():
        # Swapped coordinates to [Latitude (y), Longitude (x)] for Folium compatibility
        folium.CircleMarker(location=[row.geometry.y, row.geometry.x],
                            radius=5,color="red",fill="True",
                            fill_color="red",fill_opacity=0.7,
                            popup=f"magnitude:{row['mag']}",
                            tooltip=f"Place:{row['place']}"
                            ).add_to(m)
    return m









step_1 = get_start_end_dates()

# Unpack the inputs from step_1
start_date, end_date, magnitude = step_1

# Pass the inputs into the request_data function
step_2 = request_data(start_date, end_date, magnitude)

data=step_2

step_3=format_change(data)

gdf=step_3

step_4 = visualize_data(gdf)
step_4