import requests

print("Weather App for Maruthurai (Tiruppur)")

# API URL with coordinates for your area
url = "https://api.open-meteo.com/v1/forecast?latitude=11.1085&longitude=77.3411&current_weather=true"

try:
    response = requests.get(url)

    # Check HTTP status code
    if response.status_code == 200:
        data = response.json()

        temperature = data["current_weather"]["temperature"]
        windspeed = data["current_weather"]["windspeed"]

        print("\nWeather Data Received Successfully")
        print("Temperature:", temperature, "°C")
        print("Wind Speed:", windspeed, "km/h")

    else:
        print("API Request Failed")
        print("Status Code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Network error occurred:", e)