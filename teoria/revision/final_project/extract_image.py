"""
"""
import requests, pathlib
from PIL import Image

response = requests.get('url')

if response.status_code == 200:
    dataimg = response.content
    with open(pathlib.Path(__file__).parent / 'images' / '', 'wb') as imgfile:
        imgfile.write(dataimg)