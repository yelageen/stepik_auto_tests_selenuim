import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import math
import time

@pytest.mark.parametrize('link', [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
])

def test_stepik_param(browser, link):
    browser.get(link)

    item = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'ember32')))
    item.click()

    item = browser.find_element(By.NAME, 'login')
    item.send_keys('*@gmail.com')

    item = browser.find_element(By.NAME, 'password')
    item.send_keys('*')

    item = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    item.click()
    time.sleep(3)

    item = browser.find_element(By.CLASS_NAME, 'ember-text-area.ember-view.textarea.string-quiz__textarea')
    item.send_keys(str(math.log(int(time.time()))))
    time.sleep(3)

    item = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'submit-submission')))
    #item = browser.find_element(By.CLASS_NAME, 'submit-submission')
    item.click()
    time.sleep(5)

    item = WebDriverWait(browser, 10).until(EC.presence_of_element_located  ((By.CLASS_NAME, 'smart-hints__hint')))
    item = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint')))
    assert item.text == 'Correct!', f'[{item.text}]'

# The owls are not what they seem! OvO
