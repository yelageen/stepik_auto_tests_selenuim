from   selenium import webdriver
from   selenium.webdriver.common.by import By
import time
import unittest

class TestStepikSelenium(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self): 
        time.sleep(10)
        self.browser.quit()

    def test_registration1(self):
        self.registration('http://suninjuly.github.io/registration1.html')

    def test_registration2(self):
        self.registration('http://suninjuly.github.io/registration2.html')

    def registration(self, link):
        self.browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = self.browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control first']")
        input1.send_keys("Ivan")

        input2 = self.browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control second']")
        input2.send_keys("Petrov")

        input3 = self.browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control third']")
        input3.send_keys("Smolensk@mail.ru")

        # Отправляем заполненную форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        str1 = 'Congratulations! You have successfully registered!'
        self.assertEqual(welcome_text, str1, f'Welcome text is: "{welcome_text}", expected: "{str1}"')

if __name__ == "__main__":
    unittest.main()
