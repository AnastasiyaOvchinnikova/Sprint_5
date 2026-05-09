import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators, MainPageLocators
from helpers import generate_email
from config import PASSWORD, BASE_URL


@pytest.fixture
def driver():
    """Фикстура драйвера"""
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def created_user(driver):
    """Создание нового пользователя и возврат данных"""
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(AuthLocators.LOGIN_REGISTER_BTN)
    ).click()
    
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BTN)
    ).click()
    
    email = generate_email()  # ← используем helpers
    password = PASSWORD
    
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT)
    )
    driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*AuthLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
    
    driver.find_element(*AuthLocators.CREATE_ACCOUNT_BTN).click()
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.USER_AVATAR)
    )
    
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(AuthLocators.LOGOUT_BTN)
    ).click()
    
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(AuthLocators.LOGIN_REGISTER_BTN)
    )
    
    return {"email": email, "password": password}


@pytest.fixture
def auth_driver(driver):
    """Фикстура авторизованного пользователя"""
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(AuthLocators.LOGIN_REGISTER_BTN)
    ).click()
    
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BTN)
    ).click()
    
    email = generate_email()  # ← используем helpers
    password = PASSWORD
    
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT)
    )
    driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*AuthLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
    
    driver.find_element(*AuthLocators.CREATE_ACCOUNT_BTN).click()
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.USER_AVATAR)
    )
    
    return driver