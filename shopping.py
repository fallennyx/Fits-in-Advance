import requests
from geopy.geocoders import Nominatim

def get_shopping_info(query, location):
    api_key = "2769705d67df11795e20d4fc3a8b28f0bbf7e3cf55ef7e716d1ebef6a39d404f"
    url = f"https://serpapi.com/search.json?engine=google_shopping&q={query}&location={location}&hl=en&gl=us&api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    shopping_results = data["shopping_results"]
    info = {result["title"]: result["link"] for result in shopping_results}
    return info
#EXample
query = "ripped jeans"
location = "New York"
info = get_shopping_info(query, location)
print(info)

def get_city_from_lat_long(latitude, longitude):
    geolocator = Nominatim(user_agent="my-app")
    location = geolocator.reverse(f"{latitude}, {longitude}", exactly_one=True)
    address_components = location.raw['address']
    city = address_components.get(list(address_components)[-5], '')
    return city
#Example
latitude = 40.7128
longitude = -74.0060
result = get_city_from_lat_long(latitude, longitude)
print(result)