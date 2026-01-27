import allure
import pytest

from pages.main_page import MainPage
from pages.for_whom_page import ForWhom
from pages.about_renting import About_Renting
from data.data import *


class TestSuccessfulOrder:

    @pytest.mark.parametrize(
        "click_order, order_key",
        [
            (MainPage.click_order_top, "top"),
            (MainPage.click_order_bottom, "bottom"),
        ],
        ids=["order_top_button", "order_bottom_button"]
    )

    @allure.title("Успешный заказа самоката")
    def test_successful_order(self, driver, click_order, order_key):
        data = ORDER_DATA[order_key]
        main = MainPage(driver)
        main.open_main_page()
        click_order(main)
        
        # Заполнение первой формы
        who = ForWhom(driver)
        who.set_name(data["name"])
        who.set_surname(data["surname"])
        who.set_address(data["address"])
        who.set_phone(data["phone"])
        who.choose_metro(data["metro"])
        who.click_next()
        
        # Заполнение второй формы
        rent = About_Renting(driver)
        rent.select_a_date()
        rent.choose_rent_period(data["rent_period"])
        rent.choose_the_color_black()
        rent.write_a_comment(data["comment"])
        rent.order_button()
        rent.yes_button()
        rent.assert_view_status_button()


