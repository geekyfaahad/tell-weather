from flask import Flask, render_template, request, redirect, url_for
import requests, json
import json
import os
from api_secret import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

def get_image_url(city):
    try:
        headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
        search_url = f"https://api.unsplash.com/photos/random?query={city}&count=1&per_page=1"
        response = requests.get(search_url, headers=headers)
        data = response.json()

        if data:
            image_url = data[0]['urls']['regular']
            return image_url
        else:
            return "https://example.com/default_image.jpg"
    except Exception as e:
        print(f"Error fetching image: {e}")
        return "https://example.com/default_image.jpg" 


@app.route('/output', methods=['POST'])
def view():
    try:
        city = request.form['city']
        base_url = 'https://api.openweathermap.org/data/2.5/weather?q='
        url = f'{base_url}{city}&appid={WEATHER_API_KEY}'

        response = requests.get(url)
        data = response.json()

        if data.get('cod') == 200:
            temp = data['main']['temp']
            celsius_temp = int(temp - 273.15)
            weather_icon = data['weather'][0]['icon']
            icon_url = f'http://openweathermap.org/img/wn/{weather_icon}@2x.png'
            background_image_url = get_image_url(city)

            return render_template("output.html", result=celsius_temp, city=city, icon_url=icon_url, background_image_url=background_image_url)
        else:
            error_message = data.get('message', 'City not found')
            return render_template("index.html", error=error_message)

    except Exception as e:
        print(f"Error: {e}")
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
