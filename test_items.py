# 3.6 PyTest — параметризация, конфигурирование, плагины
#
# Задание: запуск автотестов для разных языков интерфейса.
#
# Тестируются модули:
#   - conftest.py
#   - test_items.py
#
# В файле test_items.py находится тест, который проверяет, что
# страница товара на сайте содержит кнопку добавления в корзину.
#
# Запуск в браузере Chrome (по умолчанию):
#   > pytest --language=es test_items.py
#
# Необязательно: запуск в браузере Edge:
#   > pytest --language=es --browser_name edge test_items.py
#
# Для тестирования доступны языки:
#   en-gb, es, fr, ru

from selenium.webdriver.common.by import By
import time

def test_add_to_basket_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    try:
        item = browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form > button')
    except:
        item = None
    assert item, 'The "Add to basket" button not found'
