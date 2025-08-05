from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.locators import Locators
from utils.curl import *
from utils.fixtures import driver, start_from_login_page


# Проверка перехода на главную через кнопку «Конструктор»
class TestTransitionByConstructor:
    def test_check_transition_by_constructor(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        WebDriverWait(driver, timeout=10).until(EC.url_to_be(main_site))
        driver.find_element(*Locators.button_personal_area).click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located(Locators.button_constaction))
        driver.find_element(*Locators.button_constaction).click()
        WebDriverWait(driver, timeout=10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site


# Переход на главную страницу через клик по логотипу
class TestTransitionByLogo:
    def test_transition_by_logo(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(Locators.button_personal_area)) 
        driver.find_element(*Locators.button_personal_area).click()
        WebDriverWait(driver, timeout=15).until(EC.visibility_of_element_located(Locators.inscription_profile)) 
        driver.find_element(*Locators.logo).click()
        WebDriverWait(driver, timeout=10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site


# Проверка перехода в личный кабинет
class TestCheckPageProfile:
    def test_transition_before_profile(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(Locators.inscription_bread)) 
        driver.find_element(*Locators.button_personal_area).click()
        WebDriverWait(driver, timeout=10).until(EC.url_to_be(profile_site)) 

        assert driver.current_url == (profile_site)


# Проверка выхода из личного кабинета
class TestLogout:
    def test_logout_from_profile(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        driver.find_element(*Locators.button_personal_area).click()
        button_exit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.button_exit)).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(login_site))

        assert driver.current_url == login_site
