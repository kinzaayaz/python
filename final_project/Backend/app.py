from flask import Flask, request
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def weather(country):
    import requests
    url = f"https://open-weather13.p.rapidapi.com/city/{country}/EN"
    headers = {
        "x-rapidapi-key": "0a27a5096amsha633a084ed8f456p1ce5fajsn5d3690de6f79",
        "x-rapidapi-host": "open-weather13.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

@app.route("/")
def hello_world():
    return {"message": "Welcome to weather app"}

@app.route("/get_weather", methods=["POST"])
def get_weather():
    data = request.get_json()
    city = data.get("city")  
    print(city) 
    response = weather(city)  # Use city from the request
    city_name = response.get("name", "Unknown")
    temp = response.get("main", {}).get("temp", "N/A")

    return {"City": city_name, "Temperature": temp}

if __name__ == "__main__":
    app.run(debug=True)
