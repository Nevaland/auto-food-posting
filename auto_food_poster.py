from food_crawler import food_crawling
from kko_channel_poster import kko_channel_posting

channel_posting_url = 'https://center-pf.kakao.com/_EcYKs/posts'
SCREENSHOT_FN = "screenshot.png"

if __name__ == "__main__":
    food_crawling(SCREENSHOT_FN)
    kko_channel_posting(channel_posting_url, SCREENSHOT_FN,
                        "-", "-", "Title", "Content")
