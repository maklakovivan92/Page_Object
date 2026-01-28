import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import *
from pages.base_page import BasePage


class MainPage(BasePage):
    
    
    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open(URL) 
    
    @allure.step("Открыть вопрос №{index}")
    def open_faq_question(self, index: int): 
        question_locator = (By.ID, f"accordion__heading-{index}") 
        self.scroll_to_locator(question_locator) 
        self.click(question_locator) 

    def get_faq_answer_text(self, index: int): 
        answer_locator = (By.ID, f"accordion__panel-{index}") 
        return self.get_text(answer_locator) 
    
    @allure.step("Нажать верхнюю кнопку Заказать")
    def click_order_top(self): 
        self.click(ORDER_BUTTON_TOP) 
    
    @allure.step("Нажать нижнюю кнопку Заказать")
    def click_order_bottom(self): 
        self.scroll_to_locator(ORDER_BUTTON_BOTTOM) 
        self.click(ORDER_BUTTON_BOTTOM) 
