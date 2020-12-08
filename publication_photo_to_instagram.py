import os
from dotenv import load_dotenv
from instabot import Bot


def main():
    load_dotenv()
    INSTAGRAM_USER_NAME = os.environ['INSTAGRAM_USER_NAME']
    INSTAGRAM_PASSWORD = os.environ['INSTAGRAM_PASSWORD']
    bot = Bot()
    bot.login(username=INSTAGRAM_USER_NAME, password=INSTAGRAM_PASSWORD)
    images = os.listdir("images")
    # bot.upload_photo("images_hubble/3955.jpg", caption="Nice pic!")
    for image in images:
        try:
            bot.upload_photo("images/{}".format(image), caption="Nice pic!")
        except:
            continue

if __name__ == '__main__':
    main()