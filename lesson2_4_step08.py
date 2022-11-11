from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    # wait for price to become 100
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))

    # click Book button
    item = browser.find_element(By.ID, 'book')
    item.click()

    # obtain element with a code
    x = browser.find_element(By.ID, 'input_value')

    # obtain element for entering the code
    item = browser.find_element(By.ID, 'answer')

    # enter the code
    item.send_keys(calc(x.text))

    # click Submit
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

    # obtain a code from alert and accept the alert
    alert = browser.switch_to.alert
    print(alert.text.split(':')[-1].strip())
    alert.accept()

finally:
    browser.quit()
