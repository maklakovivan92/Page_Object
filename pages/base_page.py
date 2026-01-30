from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # navigation / url 
    def open(self, url: str):
        self.driver.get(url)

    def wait_url_is(self, url: str):
        self.wait.until(EC.url_to_be(url))

    def wait_url_contains(self, text: str):
        self.wait.until(EC.url_contains(text))

    def current_url(self) -> str:
        return self.driver.current_url

    # tabs 
    def switch_to_new_tab(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

    # elements 
    def wait_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.wait_clickable(locator).click()

    def type(self, locator, text: str, clear: bool = True):
        el = self.wait_clickable(locator)
        el.click()
        if clear:
            el.clear()
        el.send_keys(text)

    def get_text(self, locator) -> str:
        return self.wait_visible(locator).text

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_to_locator(self, locator):
        el = self.wait_presence(locator)
        self.scroll_to_element(el)
    
    