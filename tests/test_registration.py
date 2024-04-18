from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
from locators import BurgersLocators
from data import BurgersTestData


class TestBurgersRegistration:

    def test_registration_positive(self, driver):
        lk_button = driver.find_element(By.XPATH, BurgersLocators.LK_BUTTON)
        lk_button.click()

        link_registration = driver.find_element(By.XPATH, BurgersLocators.LINK_REGISTRATION)
        link_registration.click()

        registration_name = driver.find_element(By.XPATH, BurgersLocators.REGISTRATION_NAME)
        registration_name.send_keys(BurgersTestData.AUTH_NAME)
        registration_email = driver.find_element(By.XPATH, BurgersLocators.REGISTRATION_EMAIL)
        registration_email.send_keys(BurgersTestData.AUTH_RANDOM_EMAIL)
        registration_password = driver.find_element(By.XPATH, BurgersLocators.REGISTRATION_PASSWORD)
        registration_password.send_keys(BurgersTestData.AUTH_PASSWORD)

        registration_button = driver.find_element(By.XPATH, BurgersLocators.REGISTRATION_BUTTON)
        registration_button.click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((
            By.XPATH, BurgersLocators.LOGIN_TITLE)))

        assert driver.find_element(By.XPATH, BurgersLocators.LOGIN_TITLE).is_displayed()

    def test_registration_negative(self, driver):
        lk_button = driver.find_element(By.XPATH, BurgersLocators.LK_BUTTON)
        lk_button.click()

        link_regostration = driver.find_element(By.XPATH, BurgersLocators.LINK_REGISTRATION)
        link_regostration.click()

        registration_name = driver.find_element(By.XPATH, BurgersLocators.REGISTRATION_NAME)
        registration_name.send_keys(BurgersTestData.AUTH_NAME)
        registration_email = driver.find_element(By.XPATH, BurgersLocators.REGISTRATION_EMAIL)
        registration_email.send_keys(BurgersTestData.AUTH_RANDOM_EMAIL)
        registration_password = driver.find_element(By.XPATH, BurgersLocators.REGISTRATION_PASSWORD)
        registration_password.send_keys(BurgersTestData.AUTH_PASSWORD_NEGATIVE)

        registration_button = driver.find_element(By.XPATH, BurgersLocators.REGISTRATION_BUTTON)
        registration_button.click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((
            By.XPATH, BurgersLocators.PASSWORD_ERROR)))

        assert driver.find_element(By.XPATH, BurgersLocators.PASSWORD_ERROR).is_displayed()
