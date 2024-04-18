from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
from locators import BurgersLocators
from data import BurgersTestData


class TestBurgersFromLkToConstruct:
    def test_go_from_lk_to_construct_button(self, driver):
        lk_button = driver.find_element(By.XPATH, BurgersLocators.LK_BUTTON)
        lk_button.click()

        login_email = driver.find_element(By.XPATH, BurgersLocators.LOGIN_EMAIL)
        login_email.send_keys(BurgersTestData.AUTH_EMAIL)
        login_password = driver.find_element(By.XPATH, BurgersLocators.LOGIN_PASSWORD)
        login_password.send_keys(BurgersTestData.AUTH_PASSWORD)

        login_button = driver.find_element(By.XPATH, BurgersLocators.LOGIN_BUTTON)
        login_button.click()

        lk_button = driver.find_element(By.XPATH, BurgersLocators.LK_BUTTON)
        lk_button.click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, BurgersLocators.SAVE_BUTTON)))

        construct_button = driver.find_element(By.XPATH, BurgersLocators.CONSTRUCT_BUTTON)
        construct_button.click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, BurgersLocators.ORDER_BUTTON)))

        order_button = driver.find_element(By.XPATH, BurgersLocators.ORDER_BUTTON)
        assert order_button.is_displayed()

    def test_go_from_lk_to_construct_logo(self, driver):
        lk_button = driver.find_element(By.XPATH, BurgersLocators.LK_BUTTON)
        lk_button.click()

        login_email = driver.find_element(By.XPATH, BurgersLocators.LOGIN_EMAIL)
        login_email.send_keys(BurgersTestData.AUTH_EMAIL)
        login_password = driver.find_element(By.XPATH, BurgersLocators.LOGIN_PASSWORD)
        login_password.send_keys(BurgersTestData.AUTH_PASSWORD)

        login_button = driver.find_element(By.XPATH, BurgersLocators.LOGIN_BUTTON)
        login_button.click()

        lk_button = driver.find_element(By.XPATH, BurgersLocators.LK_BUTTON)
        lk_button.click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, BurgersLocators.SAVE_BUTTON)))

        logo = driver.find_element(By.XPATH, BurgersLocators.LOGO)
        logo.click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, BurgersLocators.ORDER_BUTTON)))

        order_button = driver.find_element(By.XPATH, BurgersLocators.ORDER_BUTTON)
        assert order_button.is_displayed()
