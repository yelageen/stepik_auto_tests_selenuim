from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/math.html')

    # извлечь элемент с кодом
    x = browser.find_element(By.ID, 'input_value')

    # извлечь элемент для ввода кода
    item = browser.find_element(By.ID, 'answer')

    # ввести код
    item.send_keys(calc(x.text))

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
