import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from locators.for_whom_locators import *
from pages.base_page import BasePage
from data.constants import *

class ForWhom(BasePage):

    @allure.step("Открыть страницу заказа")
    def open_order_page(self):
        self.open(MAIN_URL)

    @allure.step("Ввести имя: {name}")
    def set_name(self, name: str):
        self.type(NAME_INPUT, name)

    @allure.step("Ввести фамилию: {surname}")
    def set_surname(self, surname: str):
        self.type(SURNAME_INPUT, surname)

    @allure.step("Ввести адрес: {address}")
    def set_address(self, address: str):
        self.type(ADDRESS_INPUT, address)

    @allure.step("Ввести телефон: {phone}")
    def set_phone(self, phone: str):
        self.type(PHONE_INPUT, phone)

    @allure.step("Выбрать метро: {station}")
    def choose_metro(self, station: str):
        self.type(METRO_INPUT, station)
        self.wait_clickable(METRO_INPUT).send_keys(Keys.ARROW_DOWN)
        self.wait_clickable(METRO_INPUT).send_keys(Keys.ENTER)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next(self):
        self.click(NEXT_BUTTON)

    @allure.step("Нажать на логотип 'Самокат'")
    def click_scooter_logo(self):
        self.click(LOGO_SCOOTER)

    @allure.step("Нажать на логотип 'Яндекс'")
    def click_yandex_logo(self):
        self.click(YANDEX_LOGO)

    @allure.step("Проверить, что открылась главная страница Самоката")
    def wait_main_page_opened(self):
        self.wait_url_is(MAIN_URL)

    @allure.step("Проверить, что Дзен открылся в новой вкладке")
    def wait_dzen_opened_in_new_tab(self):
        self.switch_to_new_tab()
        self.wait_url_contains(DZEN_URL_PART)


