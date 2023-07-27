import random

import requests
import os
shop_key = os.environ.get("shop_key")

class serAPI:
    def __init__(self, serAPI_key):
        self.api_key = serAPI_key

    def get_shopping_info(self, query, location):
        url = f"https://serpapi.com/search.json?engine=google_shopping&q={query}&location={location}&hl=en&gl=us&api_key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        #prnt(data)
        shopping_results = data["shopping_results"]
        info = [result["link"] for result in shopping_results]
        index =  random.randint(0,len(info))
        return info[index]