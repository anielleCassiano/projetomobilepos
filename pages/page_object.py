from selenium.webdriver.support.wait import WebDriverWait


class PageObject:
    def __init__(self, driver) -> None:
        self.driver = driver

    def find_element(self, by, value):
        return WebDriverWait(self.driver, timeout=20).until(
            lambda driver: driver.find_element(by=by, value=value))

    def close(self):
        self.driver.quit()
