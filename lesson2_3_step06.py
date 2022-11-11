from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    # click very 1st button
    item = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    item.click()

    # swith to the new tab
    browser.switch_to.window(browser.window_handles[1])

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
