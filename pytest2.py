import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class RegistrationNegativeTest(unittest.TestCase):

    def set_chrom(self):
        # Запускаем браузер Chrome
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Ждем, пока элементы загрузятся

    def test_email(self):
        driver = self.driver
        driver.get("URL_вашего_сайта")  # Замените "URL_вашего_сайта" на адрес вашего сайта

        # Заполняем поля регистрации
        username_field = driver.find_element_by_name("username")
        username_field.send_keys("test_user")

        password_field = driver.find_element_by_name("password")
        password_field.send_keys("test_password")

        confirm_password_field = driver.find_element_by_name("confirm_password")
        confirm_password_field.send_keys("test_password")

        # Нажимаем кнопку регистрации
        register_button = driver.find_element_by_xpath("//input[@type='submit']")
        register_button.click()

        # Проверяем наличие сообщения об ошибке о пустом поле адреса электронной почты
        error_message = driver.find_element_by_class_name("error-message").text
        self.assertEqual(error_message, "Введите адрес электронной почты")

    def Down(self):
        # Закрываем браузер после завершения теста
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()