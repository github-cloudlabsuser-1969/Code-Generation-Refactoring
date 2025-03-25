import requests

def get_climate_data(api_key, city_name):
    # Base URL for OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        "q": city_name,  # City name
        "appid": api_key,  # Your API key
        "units": "metric"  # Units of measurement (metric for Celsius)
    }
    
    # Make the API request
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Extract and display relevant information
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print(f"Error: Unable to fetch data. HTTP Status Code: {response.status_code}")
        print(f"Details: {response.json()}")

if __name__ == "__main__":
    # Replace 'your_api_key_here' with your actual OpenWeatherMap API key
    api_key = "723673b6005d42c3ab4c8fa3e789ada7"
    
    # Replace 'city_name_here' with the desired city name
    city_name = "Buenos Aires"
    
    get_climate_data(api_key, city_name)