from utils.locators import Locators
from utils.fixtures import driver, start_from_login_page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Активация раздела 'Булки' в конструкторе
class TestCheckChapterBread:
    def test_check_chapter_bread(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_sause)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_bread)).click()
        active_section = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.active_section))
        assert "Булки" in active_section.text


# Активация раздела 'Начинки' в конструкторе
class TestCheckChapterFillings:
    def test_check_chapter_fillings(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_sause)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_fillings)).click()
        active_section = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.active_section))
        assert "Начинки" in active_section.text


# Активация раздела 'Соусы' в конструкторе
class TestCheckChapterSauce:
    def test_check_chapter_sauce(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_fillings)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_sause)).click()
        active_section = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.active_section))
        assert "Соусы" in active_section.text
