# Import all the modules
import requests
import pandas as pd 
import time
import json
import os

# Getting the access key from a file
access_key = ""
key = open("API_KEY.txt","r")
for line in key:
    access_key=line

key.close()

print("Welcome to Weatherstack.com API")
time.sleep(2)
print("")

# Variables for JSON and CSV Files
json_file = input("Name of JSON File: ")
time.sleep(1)
csv_file = input("Name of CSV File: ")
time.sleep(1)
location = input("Which location do you want to get the weather from?: ")
time.sleep(1)

# Create the Json file 
command = f"touch {json_file}"
command2 = f"touch {csv_file}"
os.system(command)
os.system(command)

# List of weather events
weather = ["Current","Forecast"]

# Function to get the current weather
def current(access_key,json_file,csv_file,location):
    #Opening the JSON File
    inputJsonFile = open(json_file,"w")
    outputCsvFile = csv_file

    # URL for API
    url_current = "http://api.weatherstack.com/current"

    # Parameters for the API
    querystring = {"access_key": access_key, "query": location}

    # GET request from API
    response = requests.get( url_current, params=querystring)
    weatherFile = response.text
    res = json.loads(weatherFile)
    inputJsonFile.write(json.dumps(res["current"]))

    # Closing the JSON File
    inputJsonFile.close()

    # Convert JSON File to CSV File
    # pandas read JSON File
    readWeatherFile = pd.read_json(json_file)
    print(readWeatherFile)
  
    readWeatherFile.to_csv(outputCsvFile)

# Function to get the Forcast for the week
def forecast(access_key,json_file,csv_file,location):
    #Opening the JSON File
    inputJsonFile = open(json_file,"w")
    outputCsvFile = csv_file

    # URL for API
    url_current = "http://api.weatherstack.com/forecast"

    # Parameters for the API
    querystring = {"access_key": access_key, "query": location}

    # GET request from API
    response = requests.get( url_current, params=querystring)
    weatherFile = response.text
    res = json.loads(weatherFile)
    inputJsonFile.write(json.dumps(res["forecast"]))

    # Closing the JSON File
    inputJsonFile.close()

    # Convert JSON File to CSV File
    # pandas read JSON File
    readWeatherFile = pd.read_json(json_file)
    print(readWeatherFile)
  
    readWeatherFile.to_csv(outputCsvFile)

    
# Listing out the Weather Events
print("")
print("List of Weather Events:")
time.sleep(2)
print("")
for list in weather:
    print(list)
    time.sleep(1)
print(" ")
time.sleep(2)

# Asking the user what information they need
weatherEvent = input("What Type of Weather Information Do You Want: ")

if weatherEvent == "Current":
    current(access_key,json_file,csv_file,location)
elif weatherEvent == "Forecast":
    forecast(access_key,json_file,csv_file,location)



