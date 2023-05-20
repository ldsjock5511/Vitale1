import requests   #import request and json library
import json

API_KEY = "16b6bf202ce16405f080ab511914f74d"

def get_location():   # defining user prompt function

    while True:   # while loop is set to true so it will ask for a zip code or city name
        location = input("Enter a city name or zip code to search for the weather forecast in that location (q to quit): ")  # user inputs the location to search
        if location.lower() == "q":        #If user inputs a q the code will exit
            return None
        elif location.isnumeric():         # if the location is numeric it will search and return the json data for the 5 digit zip code or city name
            return {"zip": location}
        else:
            return {"q": location}    # if the user inputs a string it will search and return data for the city

def get_weather_data(location):

    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"appid": API_KEY, **location, "units": "imperial"}  # Request data in Fahrenheit and set the parameters for the function
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception if response status is not ok or un-findable
        return json.loads(response.text)  #returns json response if search is good
    except requests.exceptions.RequestException as e:     # return the value unless it comes back false
        print("Connection error:", e)   #If it does this it will print connection error return a none value, and e is the type of error  and the web site associated with it.
        return None

def print_weather_data(data):   #Defining weather data function

    if data is None:
        return
    name = data["name"]    #sets the vaiables to the json data response
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    weather_desc = data["weather"][0]["description"]
    print(f"The weather forecast in {name}, {country} is:")  #prints json data form set by code
    print(f"Actual Temp: {temp:.1f} °F")
    print(f"It feels like: {feels_like:.1f} °F")
    print(f"The student weatherman today says there will be: {weather_desc.capitalize()}")  # this will capitalize the first letter in the string

def main():  #main function loop

    print("Student Weather Forecast")
    while True:                     #setting up a while loop for the location
        location = get_location()     #location variable set to retrieve the user prompted location
        if location is None:
            break              #if return as none the program will exit
        data = get_weather_data(location)  #setting data variable to user prompted location with the retrieved data from API
        if data is None:
            print("Something went wrong and I could not get weather data. Can you please try again?")  #If the data reponse is none it will print this message
        else:
            print_weather_data(data)  #otherwise it will print the retrieved json data from api and return the values

if __name__ == "__main__":
    main()  # calling on the main function to run
