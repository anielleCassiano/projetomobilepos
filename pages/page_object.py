from selenium.webdriver.support.wait import WebDriverWait


def select_locator_by_id(locator):
    return f"br.com.brmalls.customer.amazonasshopping:id/{locator}"

def select_locator_by_text(locator):
    return f"//android.widget.TextView[@text='{locator}']"

class PageObject:
    def __init__(self, driver) -> None:
        self.driver = driver

    def find_element(self, by, value):
        return WebDriverWait(self.driver, timeout=20).until(
            lambda driver: driver.find_element(by=by, value=value))

    def find_elements(self, by, value):
        return WebDriverWait(self.driver, timeout=20).until(
            lambda driver: driver.find_elements(by=by, value=value))

    def close(self):
        self.driver.quit()
