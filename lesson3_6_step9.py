import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_lang_and_browser_from_cmd(browser):
    link = f"http://selenium1py.pythonanywhere.com/"
    print(f'Link = {link}')
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
    time.sleep(3)
