import requests
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
location = "United States"
info = get_shopping_info(query, location)
print(info)