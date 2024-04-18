from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
from locators import BurgersLocators
from data import BurgersTestData

class TestBurgersLogin:

    def test_login_enter_button(self, driver):
        enter_button = driver.find_element(By.XPATH, BurgersLocators.ENTER_BUTTON)
        enter_button.click()

        login_email = driver.find_element(By.XPATH, BurgersLocators.LOGIN_EMAIL)
        login_email.send_keys(BurgersTestData.AUTH_EMAIL)
        login_password = driver.find_element(By.XPATH, BurgersLocators.LOGIN_PASSWORD)
        login_password.send_keys(BurgersTestData.AUTH_PASSWORD)

        login_button = driver.find_element(By.XPATH, BurgersLocators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, BurgersLocators.ORDER_BUTTON)))

        order_button = driver.find_element(By.XPATH, BurgersLocators.ORDER_BUTTON)
        assert order_button.is_displayed()

    def test_login_lk_button(self, driver):
        lk_button = driver.find_element(By.XPATH, BurgersLocators.LK_BUTTON)
        lk_button.click()

        login_email = driver.find_element(By.XPATH, BurgersLocators.LOGIN_EMAIL)
        login_email.send_keys(BurgersTestData.AUTH_EMAIL)
        login_password = driver.find_element(By.XPATH, BurgersLocators.LOGIN_PASSWORD)
        login_password.send_keys(BurgersTestData.AUTH_PASSWORD)

        login_button = driver.find_element(By.XPATH, BurgersLocators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, BurgersLocators.ORDER_BUTTON)))

        order_button = driver.find_element(By.XPATH, BurgersLocators.ORDER_BUTTON)
        assert order_button.is_displayed()

    def test_login_link_enter_in_registration(self, driver):
        lk_button = driver.find_element(By.XPATH, BurgersLocators.LK_BUTTON)
        lk_button.click()

        link_registration = driver.find_element(By.XPATH, BurgersLocators.LINK_REGISTRATION)
        link_registration.click()

        link_enter = driver.find_element(By.XPATH, BurgersLocators.LINK_ENTER)
        link_enter.click()

        login_email = driver.find_element(By.XPATH, BurgersLocators.LOGIN_EMAIL)
        login_email.send_keys(BurgersTestData.AUTH_EMAIL)
        login_password = driver.find_element(By.XPATH, BurgersLocators.LOGIN_PASSWORD)
        login_password.send_keys(BurgersTestData.AUTH_PASSWORD)

        login_button = driver.find_element(By.XPATH, BurgersLocators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, BurgersLocators.ORDER_BUTTON)))

        order_button = driver.find_element(By.XPATH, BurgersLocators.ORDER_BUTTON)
        assert order_button.is_displayed()

    def test_login_link_enter_in_password_recovery(self, driver):
        lk_button = driver.find_element(By.XPATH, BurgersLocators.LK_BUTTON)
        lk_button.click()

        link_recovery = driver.find_element(By.XPATH, BurgersLocators.LINK_RECOVERY)
        link_recovery.click()

        link_enter = driver.find_element(By.XPATH, BurgersLocators.ENTER_LINK)
        link_enter.click()

        login_email = driver.find_element(By.XPATH, BurgersLocators.LOGIN_EMAIL)
        login_email.send_keys(BurgersTestData.AUTH_EMAIL)
        login_password = driver.find_element(By.XPATH, BurgersLocators.LOGIN_PASSWORD)
        login_password.send_keys(BurgersTestData.AUTH_PASSWORD)

        login_button = driver.find_element(By.XPATH, BurgersLocators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, BurgersLocators.ORDER_BUTTON)))

        order_button = driver.find_element(By.XPATH, BurgersLocators.ORDER_BUTTON)
        assert order_button.is_displayed()
