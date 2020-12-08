import requests
import os
from PIL import Image, ImageFile


def get_image(url, filepath):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)


def resize_image(image_name):
    image = Image.open(image_name)
    image = image.convert('RGB')
    image.thumbnail((1080, 1080))
    os.path.splitext(image_name)[-1]
    image.save("{}{}".format(os.path.splitext(image_name)[0], ".jpg"), format="JPEG")