import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators, MainPageLocators
from helpers import generate_email
from config import PASSWORD


class TestRegistration:
    
    def test_registration_success_avatar_displayed(self, driver):
        """Успешная регистрация: аватар отображается"""
        driver.find_element(*AuthLocators.LOGIN_REGISTER_BTN).click()
        
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BTN)
        ).click()
        
        email = generate_email()
        
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*AuthLocators.CONFIRM_PASSWORD_INPUT).send_keys(PASSWORD)
        
        driver.find_element(*AuthLocators.CREATE_ACCOUNT_BTN).click()
        
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(MainPageLocators.USER_AVATAR)
        )
        assert driver.find_element(*MainPageLocators.USER_AVATAR).is_displayed()
    
    def test_registration_success_user_name_correct(self, driver):
        """Успешная регистрация: имя пользователя содержит User"""
        driver.find_element(*AuthLocators.LOGIN_REGISTER_BTN).click()
        
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BTN)
        ).click()
        
        email = generate_email()
        
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*AuthLocators.CONFIRM_PASSWORD_INPUT).send_keys(PASSWORD)
        
        driver.find_element(*AuthLocators.CREATE_ACCOUNT_BTN).click()
        
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(MainPageLocators.USER_NAME)
        )
        user_name = driver.find_element(*MainPageLocators.USER_NAME).text
        assert "User" in user_name

    
    def test_invalid_email_fields_highlighted_red(self, driver):
        """Регистрация с некорректным email: поля выделены красным"""
        driver.find_element(*AuthLocators.LOGIN_REGISTER_BTN).click()
        
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BTN)
        ).click()
        
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys("invalid_email")
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*AuthLocators.CONFIRM_PASSWORD_INPUT).send_keys(PASSWORD)
        
        driver.find_element(*AuthLocators.CREATE_ACCOUNT_BTN).click()
        
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located(AuthLocators.ERROR_WRAPPERS)
        )
        error_elements = driver.find_elements(*AuthLocators.ERROR_WRAPPERS)
        assert len(error_elements) == 3
    
    def test_invalid_email_error_message_displayed(self, driver):
        """Регистрация с некорректным email: под полем Email отображается сообщение «Ошибка»"""
        driver.find_element(*AuthLocators.LOGIN_REGISTER_BTN).click()
        
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BTN)
        ).click()
        
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys("invalid_email")
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*AuthLocators.CONFIRM_PASSWORD_INPUT).send_keys(PASSWORD)
        
        driver.find_element(*AuthLocators.CREATE_ACCOUNT_BTN).click()
        
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AuthLocators.EMAIL_ERROR_MESSAGE)
        )
        assert error_message.is_displayed()
    
    
    def test_existing_user_fields_highlighted_red(self, driver):
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(AuthLocators.LOGIN_REGISTER_BTN)
        ).click()
    
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BTN)
        ).click()
    
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT)
        ).send_keys("test@test.ru")
    
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*AuthLocators.CONFIRM_PASSWORD_INPUT).send_keys(PASSWORD)
    
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(AuthLocators.CREATE_ACCOUNT_BTN)
        ).click()
    
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located(AuthLocators.ERROR_WRAPPERS)
        )
        error_elements = driver.find_elements(*AuthLocators.ERROR_WRAPPERS)
        assert len(error_elements) >= 3
    
    def test_existing_user_error_message_displayed(self, driver):
        """Регистрация существующего пользователя: под полем Email отображается сообщение «Ошибка»"""
        driver.find_element(*AuthLocators.LOGIN_REGISTER_BTN).click()
        
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BTN)
        ).click()
        
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys("test@test.ru")
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*AuthLocators.CONFIRM_PASSWORD_INPUT).send_keys(PASSWORD)
        
        driver.find_element(*AuthLocators.CREATE_ACCOUNT_BTN).click()
        
        error_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(AuthLocators.EMAIL_ERROR_MESSAGE)
        )
        assert error_message.is_displayed()