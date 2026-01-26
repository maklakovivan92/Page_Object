import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class About_Renting: # Детали аренды
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']") # Поле когда привезти
    DATE_30_JAN_2026 = (By.XPATH,"//div[@aria-label='Choose пятница, 30-е января 2026 г.']") # Дата
    RENT_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder") # Поле срока аренды
    BLACK_COLOR_CHECKBOX = (By.XPATH, "//label[@for='black']") # Чекбокс чёрный жемчуг
    GREY_COLOR_CHECKBOX = (By.XPATH, "//label[@for='grey']") # Чекбокс серая безысходность
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']") # Поле комментарий для курьера
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]/button[text()='Заказать']") # Кнопка заказать
    YES_BUTTON = (By.XPATH, "//button[text()='Да']") # Кнопка да
    VIEW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']") # Кнопка посмотреть статус

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Выбрать дату")
    def select_a_date(self): # Выбор даты
        self.wait.until(EC.element_to_be_clickable(self.DATE_INPUT)).click() # Ожидание и клик по полю когда привести самокат
        self.wait.until(EC.element_to_be_clickable(self.DATE_30_JAN_2026)).click() # Ожидание и клик по дате
    
    @allure.step("Выбрать срок аренды: {period_text}")
    def choose_rent_period(self, period_text): # Срок аренда
        self.wait.until(EC.element_to_be_clickable(self.RENT_PERIOD_DROPDOWN)).click() # Ожидание и клик по полю срок аренды
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class,'Dropdown-option') and text()='{period_text}']"))).click() # Ввод срока аренды
    
    @allure.step("Выбрать цвет самоката чёрный жемчуг")
    def choose_the_color_black(self): # Цвет самоката чёрный жемчуг
        self.wait.until(EC.element_to_be_clickable(self.BLACK_COLOR_CHECKBOX)).click() # Ожидание и клик по чекбоксу чёрный жемчуг
    
    @allure.step("Выбрать цвет самоката серая безысходность")
    def choose_the_color_grey(self): # Цвет самоката серая безысходность
        self.wait.until(EC.element_to_be_clickable(self.GREY_COLOR_CHECKBOX)).click() # Ожидание и клик по чекбоксу серая безысходность
    
    @allure.step("Написать комментарий: {comment}")
    def write_a_comment(self, comment): # Комментарий
        self.wait.until(EC.element_to_be_clickable(self.COMMENT_INPUT)).send_keys(comment) # Ожидание и ввод комментария
    
    @allure.step("Нажать кнопку 'Заказать'")
    def order_button(self): # Кнопка заказать
        self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON)).click() # Ожидание и клик по кнопке заказать
    
    @allure.step("Нажать кнопку 'ДА'")
    def yes_button(self): # Кнопка да
        self.wait.until(EC.element_to_be_clickable(self.YES_BUTTON)).click() # Ожидание и клик по кнопке да

    def assert_view_status_button(self): # Кнопка посмотреть статус
        visible_element = self.wait.until(EC.element_to_be_clickable(self.VIEW_STATUS_BUTTON)) # ожидаем видимость кнопки посмотреть статус
        assert visible_element.is_displayed() # Проверка что кнопка видна на экране
