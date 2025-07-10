# 🌦 WeatherBot — Flask Weather App

WeatherBot is a simple web application built with Flask that fetches and displays current weather information using the OpenWeatherMap API.

---

## 🔧 Features

- 🌤 Get real-time weather data by city name
- 📦 Built using Python + Flask + requests
- 📡 Connects to OpenWeatherMap API
- 🎨 Simple and clean UI with Jinja2 templating

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/weatherbot.git
cd weatherbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your API key

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Then edit `.env` and replace:

```
WEATHER_API_KEY=your_openweathermap_api_key
```

You can get a free API key from: https://openweathermap.org/api

### 4. Run the app locally

```bash
python app.py
```

Then go to `http://localhost:5000` in your browser.

---

## 📁 Project Structure

```
weatherbot/
│
├── app.py               # Main Flask app
├── requirements.txt     # Dependencies
├── .env.example         # Example env file
├── README.md            # This file
└── templates/
    └── index.html       # Frontend template
```

---

## 🌐 Deployment

You can easily deploy this app to platforms like:

- [Railway](https://railway.app/)
- [Render](https://render.com/)
- [Fly.io](https://fly.io/)

Just connect your GitHub repo and hit deploy!

---

## 🧠 Author

Created by [Your Name](https://github.com/yourusername)  
For learning, practice, and weather fun ☁️🌧️🌞

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
