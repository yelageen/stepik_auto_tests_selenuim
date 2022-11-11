from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    item = browser.find_element(By.NAME, 'firstname')
    item.send_keys("Ivan")

    item = browser.find_element(By.NAME, 'lastname')
    item.send_keys("Petrov")

    item = browser.find_element(By.NAME, 'email')
    item.send_keys("Smolensk@mail.ru")

    item = browser.find_element(By.XPATH, '//*[@type="file"]')  // (By.CSS_SELECTOR, "[type='file']")
    item.send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt'))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    browser.quit()
