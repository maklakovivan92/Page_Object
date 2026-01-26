import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class ForWhom: # Для кого самокат
    URL = "https://qa-scooter.praktikum-services.ru/order" # Ссылка заказа самоката
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']") # Поле Имя
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']") # Поле фамилия
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") # Поле адрес
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") # Поле телефон
    METRO_INPUT = (By.CSS_SELECTOR, "input.select-search__input") # Поле метро
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']") # Кнопка далее
    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]") # Логотип самокат
    YANDEX_LOGO = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI") # Логотип Яндекс

    def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Ввести имя: {name}")
    def set_name(self, name: str): # Ввод имени
        name_input = self.wait.until(EC.element_to_be_clickable(self.NAME_INPUT)) # Ожидаем появления поля имя
        name_input.click() # Кликаем по полю имя
        name_input.clear() # Стираем всё
        name_input.send_keys(name) # Вводим имя
    
    @allure.step("Ввести фамилию: {surname}")
    def set_surname(self, surname: str): # Ввод фамилии
        surname_input = self.wait.until(EC.element_to_be_clickable(self.SURNAME_INPUT)) # Ожидаем появления поля фамилия
        surname_input.click() # Кликаем по полю фамилия
        surname_input.clear() # Стираем всё
        surname_input.send_keys(surname) # Вводим фамилию
    
    @allure.step("Ввести адрес: {address}")
    def set_address(self, address: str): # Ввод адреса
        address_input = self.wait.until(EC.element_to_be_clickable(self.ADDRESS_INPUT)) # Ожидаем появления поля адрес
        address_input.click() # Кликаем по полю адрес
        address_input.clear() # Стираем всё
        address_input.send_keys(address) # Вводим адрес
    
    @allure.step("Ввести телефон: {phone}")
    def set_phone(self, phone: str): # Ввод телефона
        phone_input = self.wait.until(EC.element_to_be_clickable(self.PHONE_INPUT)) # Ожидаем появления поля телефона
        phone_input.click() # Кликаем по полю телефон
        phone_input.clear() # Стираем всё
        phone_input.send_keys(phone) # Вводим телефон
    
    @allure.step("Выбрать метро: {station}")
    def choose_metro(self, station: str): # Выбираем метро
        field = self.wait.until(EC.element_to_be_clickable(self.METRO_INPUT)) # Ожидаем появления поля метро
        field.click() # Кликаем по полю метро
        field.clear() # Стираем всё
        field.send_keys(station) # Вводим название станции
        field.send_keys(Keys.ARROW_DOWN) # Жмём клавишу вниз
        field.send_keys(Keys.ENTER) # Жмём клавишу enter
    
    @allure.step("Нажать кнопку 'Далее'")
    def click_next(self): # Кнопка далее
        next_button = self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON)) # Ожидаем появления кнопки далее
        next_button.click() # Кликаем на кнопку далее
    
    @allure.step("Нажать на логотип 'Самокат'")
    def click_scooter_logo(self): # Логотип самокат
         self.wait.until(EC.element_to_be_clickable(self.LOGO_SCOOTER)).click() # Ожидаем появления и клик по логотипу самокат
    
    @allure.step("Нажать на логотип 'Яндекс'")
    def click_yandex_logo(self): # Логотип Яндекс
         self.wait.until(EC.element_to_be_clickable(self.YANDEX_LOGO)).click() # Ожидаем появления и клик по логотипу Яндекс
    
    @allure.step("Открыть страницу заказа")    
    def open_order_page(self): # Страница заказа
        self.driver.get(self.URL) # Открываем страницу заказа самоката

    def wait_main_page(self): # Главная страница
        self.wait.until(EC.url_to_be('https://qa-scooter.praktikum-services.ru/')) # Ожидаем загрузки главной страницы с данным адресом

    def switch_to_new_tab(self): # Переход на новую вкладку
        self.wait.until(lambda d: len(d.window_handles) > 1) # Ожидаем вторую вкладку
        self.driver.switch_to.window(self.driver.window_handles[1]) # Переходим во вторую вкладку

    def wait_dzen_opened(self): # Страница Дзен
        self.wait.until(EC.url_contains("dzen.ru")) # Ожидаем что в ссылке будет указанный url
        
