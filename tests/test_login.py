import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators, MainPageLocators

class TestLogin:
    
    def test_login_success_avatar_displayed(self, driver, created_user):
        """Успешный вход: аватар пользователя отображается"""
        # 1. Открываем форму входа
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(AuthLocators.LOGIN_REGISTER_BTN)
        ).click()
    
        # 2. Заполняем email и пароль
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT)
        )
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(created_user["email"])
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(created_user["password"])
    
        # 3. Нажимаем кнопку "Войти"
        driver.find_element(*AuthLocators.LOGIN_BTN).click()
    
        # 4. Ждём появления аватара и проверяем, что он отображается
        avatar = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(MainPageLocators.USER_AVATAR)
        )
        assert avatar.is_displayed()
    
    def test_login_success_user_name_correct(self, driver, created_user):
        """Успешный вход: имя пользователя содержит User"""
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(AuthLocators.LOGIN_REGISTER_BTN)
        ).click()
        
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT)
        )
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(created_user["email"])
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(created_user["password"])
        
        driver.find_element(*AuthLocators.LOGIN_BTN).click()
        
        user_name_element = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(MainPageLocators.USER_NAME)
        )
        assert "User" in user_name_element.text