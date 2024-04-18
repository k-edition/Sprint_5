from selenium.webdriver.common.by import By
from conftest import driver
from locators import BurgersLocators


class TestBurgersConstruct:
    def test_go_to_sauces(self, driver):
        sauces = driver.find_element(By.XPATH, BurgersLocators.SAUCES)
        sauces.click()

        sauseces_section = driver.find_element(By.XPATH, BurgersLocators.SAUSES_SECTION)
        assert 'current' in sauseces_section.get_attribute('class')

    def test_go_to_fillings(self, driver):
        fillings = driver.find_element(By.XPATH, BurgersLocators.FILLINGS)
        fillings.click()

        fillings_section = driver.find_element(By.XPATH, BurgersLocators.FILLINGS_SECTION)
        assert 'current' in fillings_section.get_attribute('class')

    def test_go_to_rolls(self, driver):
        sauces = driver.find_element(By.XPATH, BurgersLocators.SAUCES)
        sauces.click()
        rolls = driver.find_element(By.XPATH, BurgersLocators.ROLLS)
        rolls.click()

        rolls_section = driver.find_element(By.XPATH, BurgersLocators.ROLLS_SECTION)
        assert 'current' in rolls_section.get_attribute('class')
