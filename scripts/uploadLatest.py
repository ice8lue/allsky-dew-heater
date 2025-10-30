#!/usr/bin/python

import os
import requests
import glob
from dotenv import load_dotenv
from files import latestImageFile

load_dotenv()

url = 'https://api.adfr.io/files/61badcf5-3a08-4ecb-9ca2-cebf4cdd5288'



images = glob.glob(latestImageFile)
for imageFile in images:
    with open(imageFile, 'rb') as img:
        filename = os.path.basename(imageFile)
        imageData = img.read()

        files = {
            'file': (filename, imageData, 'image/jpeg')
        }

        requests.patch(
            url, 
            files=files,
            headers={'Authorization': f'Bearer {os.getenv("DIRECTUS_API_KEY")}'}
        )
    os.remove(imageFile)