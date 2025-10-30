#!/usr/bin/python

import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = 'https://api.adfr.io/files/61badcf5-3a08-4ecb-9ca2-cebf4cdd5288'

with open('/home/adfr/tmp/latest.jpg', 'rb') as img:
    name_img= os.path.basename('/home/adfr/tmp/latest.jpg')
    files= {'image': (name_img,img,'multipart/form-data',{'Expires': '0'}) }

    requests.patch(
        url, 
        files=files,
        headers={'Authorization': f'Bearer {os.getenv("DIRECTUS_API_KEY")}'}
    )