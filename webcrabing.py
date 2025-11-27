import requests

# API endpoint
url = "https://archive-api.open-meteo.com/v1/archive"

# Query parameters
params = {
    "latitude": 24.8607,
    "longitude": 67.0011,
    "start_date": "2025-01-01",
    "end_date": "2025-01-05",
    "hourly": "temperature_2m"
}

# Send GET request
response = requests.get(url, params=params)

# Check if request worked
if response.status_code == 200:
    data = response.json()  # convert response to JSON
    print(data)
else:
    print("Error:", response.status_code)
