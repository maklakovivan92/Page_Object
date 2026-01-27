import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import *
from pages.base_page import BasePage


class MainPage(BasePage):
    
    
    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.driver.get(URL) # Открываем главную страницу
    
    @allure.step("Открыть вопрос №{index}")
    def open_faq_question(self, index: int): # Нажимаем на выбранную кнопку с вопросом
        question_locator = (By.ID, f"accordion__heading-{index}") # Локатор с выбранным вопросом
        question = self.wait.until(EC.presence_of_element_located(question_locator)) # Ждём пока кнопка появится
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question) # Прокручивем к кнопке
        self.wait.until(EC.element_to_be_clickable(question_locator)).click() # Кликаем на кнопку

    def get_faq_answer_text(self, index: int): # Получаем ответ на вопрос
        answer_locator = (By.ID, f"accordion__panel-{index}") # Локатор ответа на выбранный вопрос
        answer = self.wait.until(EC.visibility_of_element_located(answer_locator)) # Ожидаем и получем ответ на выбранный вопрос
        return answer.text # Возвращаем ответ
    
    @allure.step("Нажать верхнюю кнопку Заказать")
    def click_order_top(self): # Верхняя кнопка Заказать
        self.wait.until(EC.presence_of_element_located(ORDER_BUTTON_TOP)) # Ждём пока верхняя кнопка появится
        self.wait.until(EC.element_to_be_clickable(ORDER_BUTTON_TOP)).click() # Кликаем на верхнюю кнопку
    
    @allure.step("Нажать нижнюю кнопку Заказать")
    def click_order_bottom(self): # Нижняя кнопка Заказать
        question = self.wait.until(EC.presence_of_element_located(ORDER_BUTTON_BOTTOM)) # Ждём пока нижняя кнопка появится
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question) # Прокручивем к нижней кнопке
        self.wait.until(EC.element_to_be_clickable(ORDER_BUTTON_BOTTOM)).click() # Кликаем на нижнюю кнопку
