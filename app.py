import os
import requests
from flask import Flask, request, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("WEATHER_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None
    if request.method == "POST":
        city = request.form.get("city")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"]
            }
        else:
            error = "شهر پیدا نشد یا مشکلی در API بود."
    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)