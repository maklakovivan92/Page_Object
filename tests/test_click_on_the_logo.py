import allure
from pages.for_whom_page import *

@allure.feature("Клики по логотипам")
class TestClickOnTheLogo: # Клики по логотипам
    def test_scooter_logo(self, driver):
        page = ForWhom(driver)
        page.open_order_page()
        page.click_scooter_logo()
        page.wait_main_page()

    def test_yandex_logo(self, driver):
        page = ForWhom(driver)
        page.open_order_page()
        page.click_yandex_logo()
        page.switch_to_new_tab()
        page.wait_dzen_opened()
        assert "dzen.ru" in driver.current_url
