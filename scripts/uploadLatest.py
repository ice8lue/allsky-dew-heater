#!/usr/bin/python

import os
import requests
import glob
from dotenv import load_dotenv
from files import latestImageFile

load_dotenv()

# Directus file entry URL to update
url = 'https://api.adfr.io/files/61badcf5-3a08-4ecb-9ca2-cebf4cdd5288'


# get all images matching the pattern
images = glob.glob(latestImageFile)

# in case there are multiple, upload them all
for imageFile in images:
    with open(imageFile, 'rb') as img:
        filename = os.path.basename(imageFile)

        # read image data
        imageData = img.read()

        files = {
            'file': (filename, imageData, 'image/jpeg')
        }

        # make the PATCH request to update the image entry
        requests.patch(
            url, 
            files=files,
            headers={'Authorization': f'Bearer {os.getenv("DIRECTUS_API_KEY")}'}
        )
    
    # remove the image file after upload
    os.remove(imageFile)