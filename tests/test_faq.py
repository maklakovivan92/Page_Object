import pytest
import allure
from pages.main_page import *
from data.answer_text import *

@pytest.mark.parametrize(
    "index, expected_text",
    FAQ_ANSWERS.items(),
    ids=[f"faq_question_{i}" for i in FAQ_ANSWERS.keys()]
)

@allure.title("Ответы на Ворпосы о важном")
def test_faq_answers(driver, index, expected_text):
    page = MainPage(driver)
    page.open_main_page()
    page.open_faq_question(index)
    actual_text = page.get_faq_answer_text(index)

    assert actual_text == expected_text
    
