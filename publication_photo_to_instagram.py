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
    for image in images:
        if bot.upload_photo("images/{}".format(image), caption="Nice pic!"):
            os.remove("images/{}.REMOVE_ME".format(image))
        else:
            os.remove("images/{}".format(image))


if __name__ == '__main__':
    main()