import requests
import os
from scripts import get_image, resize_image


def get_hubble_image(image_id=1, correct_folder="images"):
    url = "http://hubblesite.org/api/v3/image/{}".format(image_id)
    response = requests.get(url, verify=False)
    response.raise_for_status()
    image = response.json()['image_files'][-1]
    exception = os.path.splitext(image['file_url'])[-1]
    url = "https:{}".format(image['file_url'])
    filename = "{}{}".format(image_id, exception)
    filepath = os.path.join(correct_folder, filename)
    get_image(url, filepath)
    resize_image(filepath)


def get_colllection_hubble_images(collection_name="holiday_cards", correct_folder="images"):
    os.makedirs(correct_folder, exist_ok=True)
    url = "http://hubblesite.org/api/v3/images/{}".format(collection_name)
    response = requests.get(url, verify=False)
    response.raise_for_status()
    for image in response.json():
        get_hubble_image(image['id'], correct_folder="images")


if __name__ == '__main__':
    get_colllection_hubble_images()