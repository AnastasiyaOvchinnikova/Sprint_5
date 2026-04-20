import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators, MainPageLocators

class TestLogout:
    
    def test_logout_success(self, auth_driver):
        """Успешный выход из аккаунта"""
        driver = auth_driver
        
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(AuthLocators.LOGOUT_BTN)
        ).click()
        
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AuthLocators.LOGIN_REGISTER_BTN)
        )
        assert driver.find_element(*AuthLocators.LOGIN_REGISTER_BTN).is_displayed()
        
        avatars = driver.find_elements(*MainPageLocators.USER_AVATAR)
        assert len(avatars) == 0 or not avatars[0].is_displayed()