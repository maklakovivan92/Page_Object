import allure
from pages.for_whom_page import *
from locators.for_whom_locators import *


class TestClickOnTheLogo: 
    @allure.title("Переход на главную по клику на логотип Самокат")
    def test_scooter_logo(self, driver):
        page = ForWhom(driver)
        page.open_order_page()
        page.click_scooter_logo()
        page.wait_main_page_opened()

        assert page.current_url() == MAIN_URL

    @allure.title("Клик по логотипу Яндекс открывает Дзен в новой вкладке")
    def test_yandex_logo(self, driver):
        page = ForWhom(driver)
        page.open_order_page()
        page.click_yandex_logo()
        page.wait_dzen_opened_in_new_tab()
        
        assert DZEN_URL_PART in page.current_url()
