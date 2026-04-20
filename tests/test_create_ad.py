from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthLocators, CreateListingLocators

class TestCreateAd:
    
    def test_create_ad_unauthorized(self, driver):
        """Создание объявления без авторизации"""
        driver.find_element(*MainPageLocators.POST_AD_BTN).click()
        
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AuthLocators.LOGIN_REGISTER_BTN)
        )
        assert driver.find_element(*AuthLocators.LOGIN_REGISTER_BTN).is_displayed()
    
    def test_create_ad_authorized(self, auth_driver):
        """Создание объявления авторизованным пользователем"""
        driver = auth_driver
        
        driver.find_element(*MainPageLocators.POST_AD_BTN).click()
        
        WebDriverWait(driver, 5).until(
            EC.url_contains("/create-lisiting")
        )
        
        ad_title = "Тест объявление"
        ad_description = "Это тестовое описание товара"
        ad_price = "1000"
        
        driver.find_element(*CreateListingLocators.TITLE_INPUT).send_keys(ad_title)
        driver.find_element(*CreateListingLocators.DESCRIPTION_INPUT).send_keys(ad_description)
        driver.find_element(*CreateListingLocators.PRICE_INPUT).send_keys(ad_price)
        
        category_arrow = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(CreateListingLocators.CATEGORY_ARROW)
        )
        category_arrow.click()
        
        tech_option = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(CreateListingLocators.CATEGORY_TECH)
        )
        tech_option.click()
        
        city_arrow = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(CreateListingLocators.CITY_ARROW)
        )
        city_arrow.click()
        
        moscow_option = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(CreateListingLocators.CITY_MOSCOW)
        )
        moscow_option.click()
        
        driver.find_element(*CreateListingLocators.CONDITION_NEW).click()
        driver.find_element(*CreateListingLocators.PUBLISH_BTN).click()
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("https://qa-desk.stand.praktikum-services.ru/")
        )
        
        avatar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.USER_AVATAR)
        )
        avatar.click()
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("/profile")
        )
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(CreateListingLocators.ALL_ADS_TITLES)
        )
        
        ad_titles = driver.find_elements(*CreateListingLocators.ALL_ADS_TITLES)
        titles_text = [title.text for title in ad_titles]
        
        assert ad_title in titles_text, f"Объявление '{ad_title}' не найдено в профиле"