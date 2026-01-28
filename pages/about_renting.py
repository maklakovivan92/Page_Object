import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.about_renting_locators import *
from pages.base_page import BasePage

class About_Renting(BasePage):  

    @allure.step("Выбрать дату")
    def select_a_date(self):
        self.click(DATE_INPUT)
        self.click(DATE_30_JAN_2026)

    @allure.step("Выбрать срок аренды: {period_text}")
    def choose_rent_period(self, period_text: str):
        self.click(RENT_PERIOD_DROPDOWN)
        self.click(rent_period_option_locator(period_text))

    @allure.step("Выбрать цвет самоката 'чёрный жемчуг'")
    def choose_the_color_black(self):
        self.click(BLACK_COLOR_CHECKBOX)

    @allure.step("Выбрать цвет самоката 'серая безысходность'")
    def choose_the_color_grey(self):
        self.click(GREY_COLOR_CHECKBOX)

    @allure.step("Написать комментарий: {comment}")
    def write_a_comment(self, comment: str):
        self.type(COMMENT_INPUT, comment, clear=True)

    @allure.step("Нажать кнопку 'Заказать'")
    def order_button(self):
        self.click(ORDER_BUTTON)

    @allure.step("Нажать кнопку 'Да'")
    def yes_button(self):
        self.click(YES_BUTTON)

    @allure.step("Дождаться появления кнопки 'Посмотреть статус'")
    def wait_view_status_button(self):
        return self.wait_clickable(VIEW_STATUS_BUTTON)
        
