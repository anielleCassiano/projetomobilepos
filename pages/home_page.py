from appium.webdriver.common.appiumby import AppiumBy

from pages.page_object import PageObject, select_locator_by_text


class HomePage(PageObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.btn_accept_cookies = select_locator_by_text("Aceitar e continuar")
        self.btn_see_more = select_locator_by_text("ver mais")
        self.welcome_message = select_locator_by_text("Olá, visitante.")
        self.btn_learn_more = select_locator_by_text("saiba mais")
        self.btn_bottom_menu = select_locator_by_text("Menu")

    def get_home(self):
        return self.find_element(AppiumBy.XPATH, self.welcome_message).text

    def accept_cookies(self):
        self.find_element(AppiumBy.XPATH, self.btn_accept_cookies).click()

    def open_our_stores_menu(self):
        self.find_element(AppiumBy.XPATH, self.btn_see_more).click()

    def open_bottom_menu(self):
        self.find_element(AppiumBy.XPATH, self.btn_bottom_menu).click()
