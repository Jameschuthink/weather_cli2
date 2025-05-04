def process_weather_data(data, latitude, longitude):
  if "error" in data:
    return f"Error: {data['error']}"
  temps = data["hourly"]["temperature_2m"]
  weather_codes = data["hourly"]["weather_code"]
  latest_index = -1
  temp = temps[latest_index]
  weather_code = weather_codes[latest_index]
  weather_desc = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast"
  }
  desc = weather_desc.get(weather_code, "Unknown")
  return f"Weather at ({latitude}, {longitude}): {temp}°C, {desc}"
