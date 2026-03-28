from flask import Flask, render_template, request
import requests
import os

api_key = os.getenv("WEATHER_API_KEY") #Fetches the api key from local env
if api_key is None:
    print(f"API Key is unavailable. Set WEATHER_API_KEY environment variable.")
    exit()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def submit():
    try:
        if request.method == "POST":
            city = request.form.get("user_input_city")
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            api_get = requests.get(url)
            data = api_get.json()

            if data["cod"] == "404":
                return render_template("index.html", error="City name invalid. Please enter a valid city name.")
            return render_template("index.html", 
                name = data['name'],
                temperature = data['main']['temp'],
                weather_condition = data['weather'][0]['description'],
                humidity = data['main']['humidity'],
                wind_speed = data['wind']['speed']
            )
        return render_template("index.html")
    except Exception as e:
        print(f"An error occurred: {e}")
        return render_template("index.html", error=f"An error occurred while fetching weather data. Please try again. Error details: {e}")
    

if __name__ == '__main__':
    app.run()