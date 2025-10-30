import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = 'https://api.adfr.io/files/61badcf5-3a08-4ecb-9ca2-cebf4cdd5288'

files = {'media': open('/home/adfr/tmp/latest.jpg', 'rb')}

requests.patch(
    url, 
    files=files,
    headers={'Authorization': f'Bearer {os.getenv("DIRECTUS_API_KEY")}'}
)