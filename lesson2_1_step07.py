from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')

    # извлечь элемент с кодом и код
    item = browser.find_element(By.ID, 'treasure')
    x = item.get_attribute('valuex')

    # извлечь элемент для ввода кода и ввести код
    item = browser.find_element(By.ID, 'answer')
    item.send_keys(calc(x))

    # кликнуть элемент Checkbox
    item = browser.find_element(By.ID, 'robotCheckbox')
    item.click()

    # кликнуть элемент Radiobutton
    item = browser.find_element(By.ID, 'robotsRule')
    item.click()

    # кликнуть Submit
    item = browser.find_element(By.CSS_SELECTOR, "button.btn")
    item.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    browser.quit()
