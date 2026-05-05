import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators, MainPageLocators

class TestLogout:
    
    def test_logout_success_login_button_displayed(self, auth_driver):
        """Успешный выход: отображается кнопка «Вход и регистрация»"""
        driver = auth_driver
        
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(AuthLocators.LOGOUT_BTN)
        ).click()
        
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(AuthLocators.LOGIN_REGISTER_BTN)
        )
        assert driver.find_element(*AuthLocators.LOGIN_REGISTER_BTN).is_displayed()
    
    def test_logout_success_avatar_not_displayed(self, auth_driver):
        """Успешный выход: аватар пользователя не отображается"""
        driver = auth_driver
        
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(AuthLocators.LOGOUT_BTN)
        ).click()
        
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(AuthLocators.LOGIN_REGISTER_BTN)
        )
        
        # Проверяем, что аватар не отображается
        avatars = driver.find_elements(*MainPageLocators.USER_AVATAR)
        assert len(avatars) == 0
    
    def test_logout_success_user_name_not_displayed(self, auth_driver):
        """Успешный выход: имя User больше не отображается"""
        driver = auth_driver
        
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(AuthLocators.LOGOUT_BTN)
        ).click()
        
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(AuthLocators.LOGIN_REGISTER_BTN)
        )
        
        # Проверяем, что имя пользователя не отображается
        user_names = driver.find_elements(*MainPageLocators.USER_NAME)
        assert len(user_names) == 0