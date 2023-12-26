from appium.webdriver.common.appiumby import AppiumBy
from pages.page_object import PageObject, select_locator_by_id, select_locator_by_text


class WelcomePage(PageObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.btn_next = select_locator_by_id("buttonNext")
        self.btn_begin = select_locator_by_id("customButtonLoadingText")
        self.btn_skip = select_locator_by_id("btSkip")

    def open_as_guest(self):
        self.find_element(AppiumBy.ID, self.btn_next).click()
        self.find_element(AppiumBy.ID, self.btn_next).click()
        self.find_element(AppiumBy.ID, self.btn_begin).click()

    def skip_welcome(self):
        self.find_element(AppiumBy.ID, self.btn_skip).click()
