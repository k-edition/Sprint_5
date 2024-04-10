from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
from locators import BurgersLocators
from data import BurgersTestData


class TestBurgersGoToLk:
    def test_go_to_lk(self, driver):
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

        lk_name = driver.find_element(By.XPATH, BurgersLocators.LK_NAME)
        assert lk_name.is_displayed() and lk_name.get_attribute('value') == 'Vera'
