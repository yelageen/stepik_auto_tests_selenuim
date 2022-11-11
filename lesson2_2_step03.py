from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    for i in range(1,3):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/selects%d.html' % i)

        # извлечь элементы с числами
        num1 = browser.find_element(By.ID, 'num1')
        num2 = browser.find_element(By.ID, 'num2')
        num = str(int(num1.text) + int(num2.text))

        # извлечь элемент для выпадающего списка
        item = browser.find_element(By.ID, 'dropdown')

        if i == 1:
            # раскрыть
            item.click()
            # кликнуть элемент списка, содержащий сумму
            item = browser.find_element(By.CSS_SELECTOR, "[value='%s']" % num)
            item.click()
        else:
            select = Select(item)
            select.select_by_value(num)

        # кликнуть Submit
        item = browser.find_element(By.CSS_SELECTOR, "button.btn")
        item.click()

        # успеваем скопировать код
        time.sleep(20)
        browser.quit()

finally:
    browser.quit()
