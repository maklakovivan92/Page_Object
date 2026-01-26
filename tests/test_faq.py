import allure
from pages.main_page import *
from data.answer_text import *

@allure.feature("Вопросы о важном")
class TestFaq: # Вопросы о важном
    def test_faq_0(self, driver):
        page = MainPage(driver)
        page.open_main_page()

        page.open_faq_question(0)
        text = page.get_faq_answer_text(0)

        assert text == answer_text_0


    def test_faq_1(self, driver):
        page = MainPage(driver)
        page.open_main_page()

        page.open_faq_question(1)
        text = page.get_faq_answer_text(1)

        assert text == answer_text_1


    def test_faq_2(self, driver):
        page = MainPage(driver)
        page.open_main_page()

        page.open_faq_question(2)
        text = page.get_faq_answer_text(2)

        assert text == answer_text_2

    def test_faq_3(self, driver):
        page = MainPage(driver)
        page.open_main_page()

        page.open_faq_question(3)
        text = page.get_faq_answer_text(3)

        assert text == answer_text_3

    def test_faq_4(self, driver):
        page = MainPage(driver)
        page.open_main_page()

        page.open_faq_question(4)
        text = page.get_faq_answer_text(4)

        assert text == answer_text_4

    def test_faq_5(self, driver):
        page = MainPage(driver)
        page.open_main_page()

        page.open_faq_question(5)
        text = page.get_faq_answer_text(5)

        assert text == answer_text_5

    def test_faq_6(self, driver):
        page = MainPage(driver)
        page.open_main_page()

        page.open_faq_question(6)
        text = page.get_faq_answer_text(6)

        assert text == answer_text_6

    def test_faq_7(self, driver):
        page = MainPage(driver)
        page.open_main_page()

        page.open_faq_question(7)
        text = page.get_faq_answer_text(7)

        assert text == answer_text_7

    
