import os
import requests
from plyer import notification 


def get_request (url,headers = None):
    if headers == None:
        response = requests.get(url)
    if headers != None:
        response = requests.get(url,headers=headers)

    if response.status_code == 200:
        return response
    else:
        request_error_notification(response.status_code,response.json()['status_message'])


def request_error_notification (status_code, status_message):
    
    title = 'Erro na requisicao HTTP'
    msg = f'Status Code: {status_code} \nMensagem: {status_message}'
    
    notification.notify(
        title=title,
        message=msg,
        app_name='alerta',
        timeout=50
    )

class Tmdb_api_key:
    def __init__(self):
        self.key = f"{os.getenv('API_KEY')}"

    def get_key(self):
        return self.key
    
    def get_headers(self):
        headers = {"accept": "application/json", 
                   "Authorization": f"Bearer {self.key}"}
        return headers