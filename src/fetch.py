import requests

def fetch_weather_data(latitude, longitude):
  url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,weather_code&timezone=Asia%2FSingapore&forecast_days=1"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  return {"error": f"Failed to fetch weather (Status: {response.status_code})"}
