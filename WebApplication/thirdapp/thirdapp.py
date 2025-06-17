from flask import Flask,render_template
import requests
import json
from weatherapi import weatherdata

secondapp = Flask(__name__)

# Homepage
@secondapp.route("/")
@secondapp.route("/homepage")
def home_page():
    return render_template("homepage.html")

# About us
@secondapp.route("/aboutus")
def about_us():
    return render_template("aboutus.html")


# Contact US
@secondapp.route("/contactus")
def contact_us():
    return render_template("contactus.html")


@secondapp.route("/data")
def data():
    weather = """{
      "dt": 1748241000,
      "sunrise": 1748217881,
      "sunset": 1748264687,
      "temp": {
        "day": 30.94,
        "min": 26.74,
        "max": 32.53,
        "night": 28.33,
        "eve": 27,
        "morn": 28.03
      },
      "feels_like": {
        "day": 37.14,
        "night": 31.47,
        "eve": 27.8,
        "morn": 31.28
      },
      "pressure": 1002,
      "humidity": 69,
      "weather": [
        {
          "id": 501,
          "main": "Rain",
          "description": "moderate rain",
          "icon": "10d"
        }
      ],
      "speed": 4.9,
      "deg": 234,
      "gust": 9.83,
      "clouds": 62,
      "pop": 1,
      "rain": 1.65
    }"""
    return weather


# view for weather data
# @secondapp.route("/weather")
# def contact_us():
#     url = "https://api.openweathermap.org/data/2.5/forecast/daily?q=vijayawada,in&cnt=10&mode=json&units=metric&APPID="
#     resp=requests.get(url)
#     data=resp.text
#     for each_dict in weather:
#     print("date :",each_dict.get('dt'),"\t","min :", each_dict.get('temp').get('min'),"\t", "max :", each_dict.get('temp').get('max'))

#     return weatherdata


if __name__ == '__main__':
	secondapp.run(debug=True)   