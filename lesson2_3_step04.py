from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    # click very 1st button
    item = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    item.click()

    # accept confirming alert
    confirm = browser.switch_to.alert
    confirm.accept()

    # obtain element with a code
    x = browser.find_element(By.ID, 'input_value')

    # obtain element for entering the code
    item = browser.find_element(By.ID, 'answer')

    # enter the code
    item.send_keys(calc(x.text))

    # click Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # obtain a code from alert and accept the alert
    alert = browser.switch_to.alert
    print(alert.text.split(':')[-1].strip())
    alert.accept()

finally:
    browser.quit()
