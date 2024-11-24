# -*- coding: utf-8 -*-
"""Api FIles

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kCv4EiXZuze26pwfL7p6jRtSQQlSYb67
"""

import requests
import json
import time

# Configuration
api_key = "fa6b3948374bc8e8ead8ef5105ba94b5"  # Replace with your actual OpenWeatherMap API key
city_name = "Karachi"  # You can change this to any city name
api_url = "http://api.openweathermap.org/data/2.5/weather"

# Function to collect data from the API
def get_weather_data(city, api_key):
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Celsius
    }
    try:
        response = requests.get(api_url, params=params)
        # Check for successful response
        if response.status_code == 200:
            return response.json()  # Return parsed JSON data
        else:
            print("Error:", response.status_code, response.text)
    except Exception as e:
        print("Error occurred:", e)

# Main program loop
if __name__ == "__main__":
    while True:
        # Collect and display data
        weather_data = get_weather_data(city_name, api_key)
        if weather_data:
            # Extracting specific data
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            weather_description = weather_data['weather'][0]['description']
            city = weather_data['name']
            country = weather_data['sys']['country']

            print(f"Weather in {city}, {country}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Description: {weather_description}")
            print("-" * 30)

        # Set a delay to avoid hitting the API rate limit
        time.sleep(60)  # 1-minute delay for periodic updates

import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "http://books.toscrape.com/"

# Send a GET request to fetch the webpage content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all books on the page
    books = soup.find_all("article", class_="product_pod")

    # Loop through each book and print the title and price
    for book in books:
        # Extract the book title
        title = book.h3.a["title"]

        # Extract the book price
        price = book.find("p", class_="price_color").get_text()

        print(f"Title: {title}")
        print(f"Price: {price}")
        print("-" * 30)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")