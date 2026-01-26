import allure
import pytest

from pages.main_page import MainPage
from pages.for_whom_page import ForWhom
from pages.about_renting import About_Renting
from data.data import *

@allure.feature("Заказ самоката")
class TestSuccessfulOrder: 
    @pytest.mark.parametrize(
        "order_button, name, surname, address, phone, metro, rent_period, color, comment",
        [
            ("top",    name_1, surname_1, address_1, phone_1, metro_1, rent_period_1_day, "black", comment_1),
            ("bottom", name_2, surname_2, address_2, phone_2, metro_2, rent_period_2_day, "grey",  comment_2),
        ],
        ids=["order_top_button", "order_bottom_button"]
    )
    def test_successful_order(self, driver, order_button, name, surname, address, phone, metro, rent_period, color, comment):
        main = MainPage(driver)
        main.open_main_page()

        
        if order_button == "top":
            main.click_order_top()
        else:
            main.click_order_bottom()

        
        who = ForWhom(driver)
        who.set_name(name)
        who.set_surname(surname)
        who.set_address(address)
        who.set_phone(phone)
        who.choose_metro(metro)
        who.click_next()

        
        rent = About_Renting(driver)
        rent.select_a_date()
        rent.choose_rent_period(rent_period)

        if color == "black":
            rent.choose_the_color_black()
        else:
            rent.choose_the_color_grey()

        rent.write_a_comment(comment)
        rent.order_button()
        rent.yes_button()

        rent.assert_view_status_button()


