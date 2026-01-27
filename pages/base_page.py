from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element
        )

    def switch_to_new_tab(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def wait_url_contains(self, text: str):
        self.wait.until(EC.url_contains(text))

    def wait_url_is(self, url: str):
        self.wait.until(EC.url_to_be(url))

    def get_current_url(self):
        return self.driver.current_url
    