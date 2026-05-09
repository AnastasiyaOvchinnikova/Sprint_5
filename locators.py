from selenium.webdriver.common.by import By

class AuthLocators:
    """Локаторы для авторизации и регистрации"""
    
    LOGIN_REGISTER_BTN = (By.XPATH, "//button[text()='Вход и регистрация']")
    NO_ACCOUNT_BTN = (By.XPATH, "//button[text()='Нет аккаунта']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//input[@name='submitPassword']")
    ERROR_WRAPPERS = (By.CLASS_NAME, "input_inputError__fLUP9")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[text()='Создать аккаунт']")
    LOGIN_BTN = (By.XPATH, "//button[text()='Войти']")
    LOGOUT_BTN = (By.XPATH, "//button[text()='Выйти']")
    EMAIL_ERROR_MESSAGE = (By.XPATH, "//span[contains(text(), 'Ошибка')]")


class MainPageLocators:
    """Локаторы главной страницы"""
    
    USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")
    USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
    POST_AD_BTN = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")


class CreateListingLocators:
    """Локаторы страницы создания объявления и профиля"""
    
    TITLE_INPUT = (By.NAME, "name")
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description']")
    PRICE_INPUT = (By.NAME, "price")
    
    CATEGORY_ARROW = (By.XPATH, "(//button[contains(@class, 'dropDownMenu_arrowDown__pfGL1')])[1]")
    CITY_ARROW = (By.XPATH, "(//button[contains(@class, 'dropDownMenu_arrowDown__pfGL1')])[2]")

    CATEGORY_TECH = (By.XPATH, "//span[text()='Технологии']")
    CATEGORY_AUTO = (By.XPATH, "//span[text()='Авто']")
    CATEGORY_BOOKS = (By.XPATH, "//span[text()='Книги']")
    CATEGORY_GARDENING = (By.XPATH, "//span[text()='Садоводство']")
    CATEGORY_HOBBY = (By.XPATH, "//span[text()='Хобби']")

    CITY_MOSCOW = (By.XPATH, "//span[text()='Москва']")
    CITY_SPB = (By.XPATH, "//span[text()='Санкт-Петербург']")
    CITY_NOVOSIBIRSK = (By.XPATH, "//span[text()='Новосибирск']")
    CITY_EKATERINBURG = (By.XPATH, "//span[text()='Екатеринбург']")
    CITY_NNOVGOROD = (By.XPATH, "//span[text()='Нижний Новгород']")
    CITY_KAZAN = (By.XPATH, "//span[text()='Казань']")

    CONDITION_NEW = (By.XPATH, "//label[text()='Новый']")
    CONDITION_USED = (By.XPATH, "//label[text()='Б/У']")

    PUBLISH_BTN = (By.XPATH, "//button[text()='Опубликовать']")

    MY_ADS_SECTION = (By.XPATH, "//h1[text()='Мои объявления']")
    
    AD_TITLE = (By.XPATH, "//*[contains(text(), 'Тест объявление')]")