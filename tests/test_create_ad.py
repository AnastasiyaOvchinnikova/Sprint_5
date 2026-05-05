from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthLocators, CreateListingLocators

class TestCreateAd:
    
    def test_create_ad_unauthorized(self, driver):
        """Создание объявления без авторизации"""
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.POST_AD_BTN)
        ).click()
        
        login_btn = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(AuthLocators.LOGIN_REGISTER_BTN)
        )
        assert login_btn.is_displayed()
    
    def test_create_ad_authorized(self, auth_driver):
        """Создание объявления авторизованным пользователем"""
        driver = auth_driver
        
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.POST_AD_BTN)
        ).click()
        
        WebDriverWait(driver, 15).until(
            EC.url_contains("/create-lisiting")
        )
        
        ad_title = "Тест объявление"
        ad_description = "Это тестовое описание товара"
        ad_price = "1000"
        
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(CreateListingLocators.TITLE_INPUT)
        ).send_keys(ad_title)
        
        driver.find_element(*CreateListingLocators.DESCRIPTION_INPUT).send_keys(ad_description)
        driver.find_element(*CreateListingLocators.PRICE_INPUT).send_keys(ad_price)
        
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(CreateListingLocators.CATEGORY_ARROW)
        ).click()
        
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(CreateListingLocators.CATEGORY_TECH)
        ).click()
        
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(CreateListingLocators.CITY_ARROW)
        ).click()
        
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(CreateListingLocators.CITY_MOSCOW)
        ).click()
        
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(CreateListingLocators.CONDITION_NEW)
        ).click()
        
        WebDriverWait(driver, 25).until(
            EC.element_to_be_clickable(CreateListingLocators.PUBLISH_BTN)
        ).click()
        
        WebDriverWait(driver, 25).until(
            EC.url_contains("education-services.ru")
        )
        
        avatar = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(MainPageLocators.USER_AVATAR)
        )
        avatar.click()
        
        WebDriverWait(driver, 30).until(
            EC.url_contains("/profile")
        )
        
        driver.refresh()
        
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Тест объявление')]"))
        )
        
        assert driver.find_element(*CreateListingLocators.AD_TITLE).is_displayed(), "Объявление 'Тест объявление' не найдено в профиле"