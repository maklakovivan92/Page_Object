import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    URL = "https://qa-scooter.praktikum-services.ru/" # Ссылка на главную страницу
    ORDER_BUTTON_TOP = (By.XPATH, "//div[starts-with(@class,'Header_Nav')]//button[normalize-space()='Заказать']") # Локатор верхней кнопки Заказать
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[starts-with(@class,'Home_FinishButton')]//button[normalize-space()='Заказать']") # Локатор нижней кнопки Заказать

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.driver.get(self.URL) # Открываем главную страницу
    
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
        self.wait.until(EC.presence_of_element_located(self.ORDER_BUTTON_TOP)) # Ждём пока верхняя кнопка появится
        self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON_TOP)).click() # Кликаем на верхнюю кнопку
    
    @allure.step("Нажать нижнюю кнопку Заказать")
    def click_order_bottom(self): # Нижняя кнопка Заказать
        question = self.wait.until(EC.presence_of_element_located(self.ORDER_BUTTON_BOTTOM)) # Ждём пока нижняя кнопка появится
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question) # Прокручивем к нижней кнопке
        self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON_BOTTOM)).click() # Кликаем на нижнюю кнопку
