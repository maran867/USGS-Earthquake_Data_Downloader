from logging import exception

import requests
import pandas as pd
import geopandas as gpd

from datetime import date
from pathlib import  Path


#STEP 1 :  USER INPUT SECTION 

def get_start_end_dates():
    #getting user input for the start date and end date and magnitude.
    while True:
       start_date=input("ENTER THE STARTING DATE HERE: in YYYY-MM-DD format (e.g. 2023-01-01): ")

       try:
           #checkiing the input date is in correct format or not 
          parsed_start_date=date.fromisoformat(start_date)
          
          if parsed_start_date != start_date :
              raise ValueError(f"{start_date} Entered date format is not correct")
          
          if parsed_start_date == start_date:
              break

       except ValueError as e:
              print(f"{e} Problem in your step 1")
              
    while True:
        #checking the end 
        end_date = input("ENTER THE ENDING DATE HERE: in YYYY-MM-DD format (e.g. 2023-01-31): ")
        parsed_end_date=date.fromisoformat(end_date)

        try:
          if end_date < start_date:
            print("End date cannot be earlier than start date. Please enter a valid end date.")

          elif  end_date != parsed_end_date:
            print(f"{end_date} Entered date format is not correct")

          else:
            break

        except exception as e:
            print(f"{e} Problem in your step 1 Ending date")

    while True:
       #checking the magnitude input is in correct format or not
        magnitude=float(input("ENTER MAGNITUDE: in decimal format (e.g. 5.0): "))
        try:
          if magnitude is None or isinstance( magnitude,float) == False:
              print(f"{magnitude} Entered magnitude format is not correct")

        except ValueError as e:
              print(f"{e} Problem in your step 1 magnitude")      

        return start_date, end_date, magnitude



#REQUESTING DATA FROM USGIS API
def request_data(start_date,end_date,magnitude):
    url=None
    response=requests.get(url) 
    data=response.json()

    return data



def save_data(data):

