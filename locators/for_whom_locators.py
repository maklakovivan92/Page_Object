from selenium.webdriver.common.by import By


NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
METRO_INPUT = (By.CSS_SELECTOR, "input.select-search__input")
NEXT_BUTTON = (By.XPATH, "//button[normalize-space()='Далее']")
LOGO_SCOOTER = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")
YANDEX_LOGO = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
