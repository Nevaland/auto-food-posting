from io import BytesIO
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium import webdriver

import sys
import os
from time import sleep

URL = 'https://www.gntp.or.kr/board/list'
SCREENSHOT_FN = "screenshot.png"


def food_crawling():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--log-level=3')
    options.add_argument('--disable-logging')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')

    if getattr(sys, 'frozen', False):
        chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
        driver = webdriver.Chrome(
            executable_path=chromedriver_path, options=options)
    else:
        driver = webdriver.Chrome(
            executable_path="chromedriver", options=options)

    driver.implicitly_wait(3)
    driver.get(url=URL)
    driver.execute_script("goPage('S', {boardType:'notice'}, '/board/list')")

    trs_as_posts = driver.find_elements_by_css_selector(
        "body > section > div.contents > div.big-container > div.contentPage > div.de-news > table > tbody > tr")
    for tr_as_post in trs_as_posts:
        post_name = tr_as_post.find_element_by_css_selector(
            "td.de-writeless > a").text
        if "식단표" in post_name:
            script_to_connect_post = tr_as_post.find_element_by_css_selector(
                "td.de-writeless > a").get_attribute('onclick')
            break
    driver.execute_script(script_to_connect_post)

    script_to_connect_content = driver.find_element_by_css_selector(
        "body > section > div.contents > div.big-container > table.de-biz-table > tbody > tr:nth-child(2) > td:nth-child(3) > button:nth-child(2)").get_attribute('onclick')
    driver.execute_script(script_to_connect_content)

    while len(driver.window_handles) == 1:
        sleep(1)
    driver.switch_to.window(driver.window_handles[-1])

    sleep(2)
    png = driver.get_screenshot_as_png()
    im = Image.open(BytesIO(png))
    region = im.crop((55, 40, im.size[0]-55, im.size[1]-40))
    region.save(SCREENSHOT_FN)

    driver.close()
    driver.switch_to.window(driver.window_handles[-1])
    driver.close()


if __name__ == "__main__":
    food_crawling()
