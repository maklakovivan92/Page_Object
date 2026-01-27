import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.about_renting_locators import *
from pages.base_page import BasePage

class About_Renting(BasePage): # Детали аренды
    
    @allure.step("Выбрать дату")
    def select_a_date(self): # Выбор даты
        self.wait.until(EC.element_to_be_clickable(DATE_INPUT)).click() # Ожидание и клик по полю когда привести самокат
        self.wait.until(EC.element_to_be_clickable(DATE_30_JAN_2026)).click() # Ожидание и клик по дате
    
    @allure.step("Выбрать срок аренды: {period_text}")
    def choose_rent_period(self, period_text): # Срок аренда
        self.wait.until(EC.element_to_be_clickable(RENT_PERIOD_DROPDOWN)).click() # Ожидание и клик по полю срок аренды
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class,'Dropdown-option') and text()='{period_text}']"))).click() # Ввод срока аренды
    
    @allure.step("Выбрать цвет самоката чёрный жемчуг")
    def choose_the_color_black(self): # Цвет самоката чёрный жемчуг
        self.wait.until(EC.element_to_be_clickable(BLACK_COLOR_CHECKBOX)).click() # Ожидание и клик по чекбоксу чёрный жемчуг
    
    @allure.step("Выбрать цвет самоката серая безысходность")
    def choose_the_color_grey(self): # Цвет самоката серая безысходность
        self.wait.until(EC.element_to_be_clickable(GREY_COLOR_CHECKBOX)).click() # Ожидание и клик по чекбоксу серая безысходность
    
    @allure.step("Написать комментарий: {comment}")
    def write_a_comment(self, comment): # Комментарий
        self.wait.until(EC.element_to_be_clickable(COMMENT_INPUT)).send_keys(comment) # Ожидание и ввод комментария
    
    @allure.step("Нажать кнопку 'Заказать'")
    def order_button(self): # Кнопка заказать
        self.wait.until(EC.element_to_be_clickable(ORDER_BUTTON)).click() # Ожидание и клик по кнопке заказать
    
    @allure.step("Нажать кнопку 'ДА'")
    def yes_button(self): # Кнопка да
        self.wait.until(EC.element_to_be_clickable(YES_BUTTON)).click() # Ожидание и клик по кнопке да

    def assert_view_status_button(self): # Кнопка посмотреть статус
        self.wait.until(EC.element_to_be_clickable(VIEW_STATUS_BUTTON)) # ожидаем видимость кнопки посмотреть статус
        
