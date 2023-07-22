# File: api_handler.py

import requests

def make_api_request(url, params=None):
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        # Process the data or return it to the caller
        return data
    else:
        # Handle the API error appropriately
        print(f"API request failed with status code {response.status_code}")
        return None
