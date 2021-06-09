import os
from auto_food_poster import SCREENSHOT_FN
from food_crawler import food_crawling


def test_food_crawling():
    if os.path.isfile(SCREENSHOT_FN):
        os.remove(SCREENSHOT_FN)
    food_crawling()
    if not os.path.isfile(SCREENSHOT_FN):
        return False
    return True


if __name__ == "__main__":
    if test_food_crawling():
        print("[SUCCESS] food_crawling() geneated " + SCREENSHOT_FN + " File.")
    else:
        print("[ERROR] food_crawling() failed to geneate " +
              SCREENSHOT_FN + " File.")
