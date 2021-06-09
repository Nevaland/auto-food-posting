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

PRE_URL = 'https://accounts.kakao.com/login/kakaobusiness?continue='


def kko_channel_posting(channel_posting_url, screenshot_fn, kko_email, kko_password, title, content):
    URL = PRE_URL + channel_posting_url
    SCREENSHOT_FN_DIR = os.path.abspath(screenshot_fn)

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
    # WebDriverWait(driver, sys.maxsize).until(
    #     lambda driver: driver.current_url == channel_posting_url)

    driver.find_element_by_name('email').send_keys(kko_email)
    driver.find_element_by_name('password').send_keys(kko_password)
    driver.find_element_by_css_selector(
        '#login-form > fieldset > div.wrap_btn > button.btn_g.btn_confirm.submit').click()

    sleep(3)
    for _ in range(5):
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    # Title
    driver.find_element_by_css_selector(
        '#mArticle > div > div > div:nth-child(1) > div > form > div.tit_tf > input').send_keys(title)
    # Content
    if content != "":
        driver.find_element_by_css_selector(
            '#mArticle > div > div > div:nth-child(1) > div > form > div.desc_tf > div > div > div > div > textarea').send_keys(content)
    # Image
    driver.find_element_by_css_selector(
        '#mArticle > div > div > div:nth-child(1) > div > form > ul > li:nth-child(1) > div > input').send_keys(SCREENSHOT_FN_DIR)
    # Submit
    driver.find_element_by_css_selector(
        '#mArticle > div > div > div:nth-child(1) > div > form > div:nth-child(4) > div.foot_write > div.wrap_btn > button.btn_g.btn_g2').click()

    driver.close()
