import requests
from datetime import datetime, timedelta
import time

def get_questions(tag):
    from_date = int((datetime.now() - timedelta(days=2)).timestamp())
    url = f'https://api.stackexchange.com/2.3/search?fromdate={from_date}&order=desc&sort=activity&tagged={tag}&site=stackoverflow'
    response = requests.get(url)
    json = response.json()

    if response.status_code == 200:
        for question in json['items']:
            print(question['title'])

get_questions('python')