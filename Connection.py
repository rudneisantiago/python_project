import os
import requests

class Connection:
    def __init__(self):
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {os.getenv('API_KEY')}"
        }

    def authenticate(self):
        url = "https://api.themoviedb.org/3/authentication"
        response = requests.get(url, headers=self.headers)
        print(response.text)

    def get(self, url):
        response = requests.get(f"https://api.themoviedb.org/3/{url}", headers=self.headers)
        return response.json()
