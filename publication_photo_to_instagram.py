import os
from pathlib import Path
from dotenv import load_dotenv
from instabot import Bot



def main():
    IMAGES_DIR = Path.cwd().joinpath('images')
    load_dotenv()
    INSTAGRAM_USER_NAME = os.environ['INSTAGRAM_USER_NAME']
    INSTAGRAM_PASSWORD = os.environ['INSTAGRAM_PASSWORD']
    bot = Bot()
    bot.login(username=INSTAGRAM_USER_NAME, password=INSTAGRAM_PASSWORD)
    images = os.listdir("images")
    for image in images:
        image_path = IMAGES_DIR.joinpath(image)
        if bot.upload_photo(image_path, caption="Nice pic!"):
            os.remove("{}.REMOVE_ME".format(image_path))
        else:
            os.remove(image_path)


if __name__ == '__main__':
    main()