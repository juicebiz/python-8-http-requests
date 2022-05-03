import os
from dotenv import load_dotenv
import requests
YANDEX_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        link = self._get_upload_link(file_path)
        params = {
            'path': '/',
            'overwrite': True,
            'url': f'{YANDEX_URL}'
        }
        response = requests.put(link, data=open(file_path, 'rb'), headers=self._get_headers(), params=params)
        if response.status_code == 201:
            print('Загрузка завершена')

    def _get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, file_path: str):
        url = f'{YANDEX_URL}'
        params = {
            'path': file_path,
            'overwrite': True
        }
        response = requests.get(url, headers=self._get_headers(), params=params)
        if(response.status_code == 200):
            json = response.json()
            return json['href']
        else:
            print('Ошибка')

if __name__ == '__main__':
    load_dotenv()
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'file_for_upload.txt'
    token = os.environ.get('API_KEY')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)