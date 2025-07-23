import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.email_password_generator import EmailPasswordGenerator
from utils.locators import Locators
from utils.fixtures import driver, register_new_account, start_from_main_not_login
from utils.data import Credantial
from utils.curl import *


# Успешная регистрация нового пользователя
@pytest.mark.usefixtures("register_new_account")
class TestRegistrationNewUser:
    def test_registration(self, register_new_account):
        driver, email, password = register_new_account
        driver.maximize_window()

        driver.find_element(*Locators.button_personal_area).click()
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.field_password).send_keys(password)
        driver.find_element(*Locators.button_entrance).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))
        assert driver.current_url == main_site


# Попытка зарегистрировать существующего пользователя
@pytest.mark.usefixtures("start_from_main_not_login")
class TestExistingAccount:
    def test_existing_account(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()

        driver.find_element(*Locators.button_personal_area).click()
        driver.find_element(*Locators.inscription_login).click()
        driver.find_element(*Locators.field_name).send_keys(Credantial.name)
        driver.find_element(*Locators.field_email).send_keys(Credantial.email)
        driver.find_element(*Locators.field_password).send_keys(Credantial.password)
        driver.find_element(*Locators.button_register).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.inscription_error_account))


# Проверка валидации поля "Пароль"
@pytest.mark.usefixtures("start_from_main_not_login")
class TestInvalidPassword:
    def test_invalid_password(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()

        driver.find_element(*Locators.button_personal_area).click()
        driver.find_element(*Locators.inscription_login).click()
        driver.find_element(*Locators.field_name).send_keys(Credantial.name)
        driver.find_element(*Locators.field_email).send_keys(Credantial.email)
        driver.find_element(*Locators.field_password).send_keys("help")  # Пароль должен быть не менее 6 символов
        driver.find_element(*Locators.button_register).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_error_password))


# Проверка регистрации без пароля
@pytest.mark.usefixtures("start_from_main_not_login")
class TestMissingPassword:
    def test_missing_password(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()
        email = EmailPasswordGenerator().generate()[0]

        driver.find_element(*Locators.button_personal_area).click()
        driver.find_element(*Locators.inscription_login).click()
        driver.find_element(*Locators.field_name).send_keys(Credantial.name)
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.button_register).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(register_site))
        assert driver.current_url == register_site


# Проверка регистрации без email
@pytest.mark.usefixtures("start_from_main_not_login")
class TestMissingEmail:
    def test_missing_email(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()
        generator = EmailPasswordGenerator()
        password = generator.generate()

        driver.find_element(*Locators.button_personal_area).click()
        driver.find_element(*Locators.inscription_login).click()
        driver.find_element(*Locators.field_name).send_keys(Credantial.name)
        driver.find_element(*Locators.field_password).send_keys(password)
        driver.find_element(*Locators.button_register).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(register_site))
        assert driver.current_url == register_site


# Проверка регистрации без имени
@pytest.mark.usefixtures("start_from_main_not_login")
class TestMissingName:
    def test_missing_name(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()
        generator = EmailPasswordGenerator()
        email, password = generator.generate()

        driver.find_element(*Locators.button_personal_area).click()
        driver.find_element(*Locators.inscription_login).click()
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.field_password).send_keys(password)
        driver.find_element(*Locators.button_register).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(register_site))
        assert driver.current_url == register_site
