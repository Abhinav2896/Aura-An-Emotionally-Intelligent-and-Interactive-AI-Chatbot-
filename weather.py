import requests

def get_weather():
    city = "Delhi"
    API_KEY = "YOUR_OPENWEATHERMAP_KEY"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()
    temp = res['main']['temp']
    desc = res['weather'][0]['description']
    print(f"Weather: {temp}°C, {desc}")