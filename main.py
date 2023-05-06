import tkinter as tk
import requests
from datetime import datetime

def display_weather():
    location = location_entry.get()
    api_key = "a8b83d9e434adb97d352e555f8f13fab"
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(location, api_key)
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    if api_data['cod']==404:
        error_label.config(text="Invalid city name", fg="red")
    else:
        temp_city= ((api_data['main']['temp'])-273.15)
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_speed = api_data['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
        temp_label.config(text="Current temperature is: {:.2f} deg C".format(temp_city))
        desc_label.config(text="Current weather desc  : {}".format(weather_desc))
        hum_label.config(text="Current Humidity      : {}%".format(hmdt))
        wind_label.config(text="Current wind speed    : {} kmph".format(wind_speed))
        date_label.config(text="{}".format(date_time))
        error_label.config(text="")

window = tk.Tk()
window.geometry("500x400")
window.configure(bg="PaleGreen4")
window.title("Weather App")

title_label = tk.Label(window, text="Weather monitor", font=("Courier", 24), bg="DarkSeaGreen1")
title_label.pack(pady=20)

location_frame = tk.Frame(window, bg="#e6f7ff")
location_frame.pack(pady=10)

location_label = tk.Label(location_frame, text="Enter city name:", font=("Arial", 14), bg="coral4")
location_label.pack(side=tk.LEFT)

location_entry = tk.Entry(location_frame, font=("Arial", 14), width=20)
location_entry.pack(side=tk.LEFT, padx=10)

fetch_button = tk.Button(window, text="Fetch Weather", font=("Arial", 14), command=display_weather)
fetch_button.pack(pady=20)

data_frame = tk.Frame(window, bg="#e6f7ff")
data_frame.pack()

temp_label = tk.Label(data_frame, text="", font=("Arial", 14), bg="#e6f7ff")
temp_label.pack(pady=10)

desc_label = tk.Label(data_frame, text="", font=("Arial", 14), bg="#e6f7ff")
desc_label.pack(pady=10)

hum_label = tk.Label(data_frame, text="", font=("Arial", 14), bg="#e6f7ff")
hum_label.pack(pady=10)

wind_label = tk.Label(data_frame, text="", font=("Arial", 14), bg="#e6f7ff")
wind_label.pack(pady=10)

date_label = tk.Label(window, text="", font=("Arial", 14), bg="#e6f7ff")
date_label.pack(pady=10)

error_label = tk.Label(window, text="", font=("Arial", 14), bg="#e6f7ff")
error_label.pack(pady=10)

window.mainloop()
