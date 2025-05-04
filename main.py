# Runs the Weather CLI
from src.fetch import fetch_weather_data
from src.process import process_weather_data

def main():
  """Fetch and display weather for default coordinates."""
  latitude = 2.5
  longitude = 112.5
  data = fetch_weather_data(latitude, longitude)
  result = process_weather_data(data, latitude, longitude)
  print(result)

if __name__ == "__main__":
  main()
