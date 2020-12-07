import requests
import os
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


def get_spacex_images(correct_folder="images"):
    os.makedirs(correct_folder, exist_ok=True)
    space_links = fetch_spacex_last_launch()
    for link_number, link in enumerate(space_links):
        filename = "space{}.jpg".format(link_number)
        filepath = os.path.join(correct_folder, filename)
        get_image(link, filepath)
        resize_image(filepath)


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v4/launches/latest"
    response = requests.get(url, verify=False)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def get_image(url, filepath):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)


def resize_image(image_name):
    image = Image.open(image_name)
    image = image.convert('RGB')
    image.thumbnail((1080, 1080))
    image.save("{}.{}".format(image_name.split(".")[0],"jpg"), format="JPEG")


if __name__ == '__main__':
    get_spacex_images()