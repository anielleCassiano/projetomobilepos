from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from pages.page_object import PageObject, select_locator_by_text


class MenuPage(PageObject):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.cinema = select_locator_by_text("Cinema")

    def open_movies(self):
        self.find_element(AppiumBy.XPATH, self.cinema).click()

