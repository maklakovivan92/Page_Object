from selenium.webdriver.common.by import By


DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
DATE_30_JAN_2026 = (By.XPATH, "//div[@aria-label='Choose пятница, 30-е января 2026 г.']")
RENT_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
BLACK_COLOR_CHECKBOX = (By.XPATH, "//label[@for='black']")
GREY_COLOR_CHECKBOX = (By.XPATH, "//label[@for='grey']")
COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[normalize-space()='Заказать']")
YES_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Modal')]//button[normalize-space()='Да']")
VIEW_STATUS_BUTTON = (By.XPATH, "//button[normalize-space()='Посмотреть статус']")
ORDER_DONE_TITLE = (By.CLASS_NAME, "Order_ModalHeader")  

def rent_period_option_locator(period_text: str):
    return (By.XPATH, f"//div[contains(@class,'Dropdown-option') and normalize-space()='{period_text}']")
