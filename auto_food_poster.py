from food_crawler import food_crawling
from kko_channel_poster import kko_channel_posting

import json

SCREENSHOT_FN = "screenshot.png"


if __name__ == "__main__":
    try:
        with open('config.json') as f:
            CONFIG = json.load(f)
    except FileNotFoundError:
        kko_email = input("KAKAO EMAIL: ")
        kko_password = input("Password: ")
        channel_posting_url = input(
            "Channel Posting URL (ex. 'https://center-pf.kakao.com/_EcYKs/posts' ): ")
        CONFIG = {
            "channel_posting_url": channel_posting_url,
            "kko_email": kko_email,
            "kko_password": kko_password
        }
        with open('config.json', 'w') as f:
            json.dump(CONFIG, f)

    post_name = food_crawling(SCREENSHOT_FN)
    post_title = "[" + \
        post_name[post_name.rfind('(')+1: post_name.rfind(')')] + "]"
    kko_channel_posting(CONFIG['channel_posting_url'], SCREENSHOT_FN,
                        CONFIG['kko_email'], CONFIG['kko_password'], post_title, "")
