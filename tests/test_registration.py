import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators, MainPageLocators

PASSWORD = "Test123456"


class TestRegistration:
    
    def test_registration_success(self, driver, generate_email):
        """Успешная регистрация нового пользователя"""
        driver.find_element(*AuthLocators.LOGIN_REGISTER_BTN).click()
        
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BTN)
        ).click()
        
        email = generate_email()
        
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*AuthLocators.CONFIRM_PASSWORD_INPUT).send_keys(PASSWORD)
        
        driver.find_element(*AuthLocators.CREATE_ACCOUNT_BTN).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.USER_AVATAR)
        )
        assert driver.find_element(*MainPageLocators.USER_AVATAR).is_displayed()
        
        user_name = driver.find_element(*MainPageLocators.USER_NAME).text
        assert "User" in user_name
    
    def test_registration_invalid_email(self, driver):
        """Регистрация с некорректным email"""
        driver.find_element(*AuthLocators.LOGIN_REGISTER_BTN).click()
        
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BTN)
        ).click()
        
        invalid_email = "invalid_email"
        
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(invalid_email)
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*AuthLocators.CONFIRM_PASSWORD_INPUT).send_keys(PASSWORD)
        
        driver.find_element(*AuthLocators.CREATE_ACCOUNT_BTN).click()
        
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AuthLocators.ERROR_MESSAGE)
        )
        error_text = driver.find_element(*AuthLocators.ERROR_MESSAGE).text
        assert "Ошибка" in error_text or "error" in error_text.lower()
        
        error_elements = driver.find_elements(*AuthLocators.ERROR_WRAPPERS)
        assert len(error_elements) >= 3
    
    def test_registration_existing_user(self, driver):
        """Регистрация уже существующего пользователя"""
        driver.find_element(*AuthLocators.LOGIN_REGISTER_BTN).click()
        
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BTN)
        ).click()
        
        existing_email = "test@test.ru"
        
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(existing_email)
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*AuthLocators.CONFIRM_PASSWORD_INPUT).send_keys(PASSWORD)
        
        driver.find_element(*AuthLocators.CREATE_ACCOUNT_BTN).click()
        
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AuthLocators.ERROR_MESSAGE)
        )
        error_text = driver.find_element(*AuthLocators.ERROR_MESSAGE).text
        assert "Ошибка" in error_text or "error" in error_text.lower()
        
        error_elements = driver.find_elements(*AuthLocators.ERROR_WRAPPERS)
        assert len(error_elements) >= 3