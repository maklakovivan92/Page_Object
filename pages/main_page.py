import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import *
from pages.base_page import BasePage
from data.constants import *


class MainPage(BasePage):
    
    
    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open(MAIN_URL) 
    
    @allure.step("Открыть вопрос №{index}")
    def open_faq_question(self, index: int):
        locator = faq_question_locator(index)
        self.scroll_to_locator(locator)
        self.click(locator)

    def get_faq_answer_text(self, index: int) -> str:
        locator = faq_answer_locator(index)
        return self.get_text(locator)
    
    @allure.step("Нажать верхнюю кнопку Заказать")
    def click_order_top(self): 
        self.click(ORDER_BUTTON_TOP) 
    
    @allure.step("Нажать нижнюю кнопку Заказать")
    def click_order_bottom(self): 
        self.scroll_to_locator(ORDER_BUTTON_BOTTOM) 
        self.click(ORDER_BUTTON_BOTTOM) 

