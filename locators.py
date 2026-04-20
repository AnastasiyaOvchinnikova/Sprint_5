from selenium.webdriver.common.by import By

class AuthLocators:
    """Локаторы для авторизации и регистрации"""
    
    LOGIN_REGISTER_BTN = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    NO_ACCOUNT_BTN = (By.XPATH, "//*[@id='root']/div/div[2]/div[5]/form/div[3]/button[2]")
    EMAIL_INPUT = (By.XPATH, "//*[@id='root']/div/div[2]/div[5]/form/div[2]/div[1]/div/div/input")
    PASSWORD_INPUT = (By.XPATH, "//*[@id='root']/div/div[2]/div[5]/form/div[2]/div[2]/div/div/input")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//*[@id='root']/div/div[2]/div[5]/form/div[2]/div[3]/div/div/input")
    ERROR_WRAPPERS = (By.CLASS_NAME, "input_inputError__fLUP9")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//*[@id='root']/div/div[2]/div[5]/form/div[3]/button[1]")
    LOGIN_BTN = (By.XPATH, "//button[text()='Войти']")
    LOGOUT_BTN = (By.XPATH, "//*[@id='root']/div/div[1]/div/div[1]/div/button")
    ERROR_MESSAGE = (By.XPATH, "//*[@id='root']/div/div[2]/div[5]/form/div[2]/div[1]/span")


class MainPageLocators:
    """Локаторы главной страницы"""
    
    USER_AVATAR = (By.XPATH, "//*[@id='root']/div/div[1]/div/div[1]/button")
    USER_NAME = (By.XPATH, "//*[@id='root']/div/div[1]/div/div[1]/div/h3")
    POST_AD_BTN = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")


class CreateListingLocators:
    """Локаторы страницы создания объявления и профиля"""
    
    # Поля формы
    TITLE_INPUT = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[2]/div[1]/div/div/input")
    DESCRIPTION_INPUT = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[4]/div/textarea")
    PRICE_INPUT = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[5]/div/div/input")
    
    # Стрелочки для открытия dropdown
    CATEGORY_ARROW = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[2]/div[2]/div[1]/button")
    CITY_ARROW = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[3]/div[1]/button")
    
    # Опции категорий
    CATEGORY_TECH = (By.XPATH, "//span[text()='Технологии']")
    CATEGORY_AUTO = (By.XPATH, "//span[text()='Авто']")
    CATEGORY_BOOKS = (By.XPATH, "//span[text()='Книги']")
    CATEGORY_GARDENING = (By.XPATH, "//span[text()='Садоводство']")
    CATEGORY_HOBBY = (By.XPATH, "//span[text()='Хобби']")
    
    # Опции городов
    CITY_MOSCOW = (By.XPATH, "//span[text()='Москва']")
    CITY_SPB = (By.XPATH, "//span[text()='Санкт-Петербург']")
    CITY_NOVOSIBIRSK = (By.XPATH, "//span[text()='Новосибирск']")
    CITY_EKATERINBURG = (By.XPATH, "//span[text()='Екатеринбург']")
    CITY_NNOVGOROD = (By.XPATH, "//span[text()='Нижний Новгород']")
    CITY_KAZAN = (By.XPATH, "//span[text()='Казань']")
    
    # Состояние товара
    CONDITION_NEW = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/fieldset/div/div[1]")
    CONDITION_USED = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/fieldset/div/div[2]")
    
    # Кнопка публикации
    PUBLISH_BTN = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/button")
    
    # Блок "Мои объявления" в профиле (заголовок)
    MY_ADS_SECTION = (By.XPATH, "//*[@id='root']/div/div[2]/div[4]/h1")
    
    # Все заголовки объявлений в блоке "Мои объявления" (ДОБАВЛЕНО!)
    ALL_ADS_TITLES = (By.XPATH, "//*[@id='root']/div/div[2]/div[4]/div/div//h2")