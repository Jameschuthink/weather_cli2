<<<<<<< HEAD
# weather_cli2
=======
 A simple command-line tool to fetch and display weather data using the Open-Meteo API.

 ## Setup

 1. Install dependency:
    ```bash
    python3 -m pip install -r requirements.txt
    ```
 2. Run the tool:
    ```bash
    python3 main.py
    ```

 ## Output

 Displays weather for coordinates (2.5, 112.5), e.g.:
 ```
 Weather at (2.5, 112.5): 26.5°C, Clear sky
 ```

 ## Structure

 - `src/fetch.py`: Fetches API data.
 - `src/process.py`: Formats data for display.
 - `main.py`: Runs the program.
>>>>>>> 3efaf1d (Add Weather CLI with modular structure)
