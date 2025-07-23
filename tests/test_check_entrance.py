from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.locators import Locators
from utils.curl import *
from utils.data import Credantial
from utils.fixtures import driver, start_from_login_page, start_from_main_not_login, start_from_recovery_page
from utils.fixtures import start_from_main_not_login


# Проверка выхода из аккаунта
class TestButtonCheckExit:
    def test_check_logging_out(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_bread))
        driver.find_element(*Locators.button_personal_area).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_profile))
        driver.find_element(*Locators.button_exit).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(login_site))

        assert driver.current_url == login_site


# Вход через большую кнопку "Войти в аккаунт" на главной
class TestBigMainButton:
    def test_check_entrance_by_big_button(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()

        driver.find_element(*Locators.entrance_on_the_main).click()
        driver.find_element(*Locators.field_email).send_keys(Credantial.email)
        driver.find_element(*Locators.field_password).send_keys(Credantial.password)
        driver.find_element(*Locators.button_entrance).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site


# Восстановление пароля и вход
class TestCheckRegister:
    def test_login_password_recovery(self, start_from_recovery_page):
        driver = start_from_recovery_page
        driver.maximize_window()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.inscription_bread))

        assert driver.current_url == main_site


# Проверка входа через ссылки "Зарегистрироваться"
class TestCheckEntranceFromRecoveryPage:
    def test_button_inscription_login(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()

        driver.find_element(*Locators.button_personal_area).click()
        driver.find_element(*Locators.inscription_login).click()
        driver.find_element(*Locators.inscription_button_entrance).click()
        driver.find_element(*Locators.field_email).send_keys(Credantial.email)
        driver.find_element(*Locators.field_password).send_keys(Credantial.password)
        driver.find_element(*Locators.button_entrance).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site
