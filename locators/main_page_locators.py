from selenium.webdriver.common.by import By


ORDER_BUTTON_TOP = (By.XPATH, "//div[starts-with(@class,'Header_Nav')]//button[normalize-space()='Заказать']")
ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[starts-with(@class,'Home_FinishButton')]//button[normalize-space()='Заказать']")
URL = "https://qa-scooter.praktikum-services.ru/"
