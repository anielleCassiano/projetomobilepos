from appium.webdriver.common.appiumby import AppiumBy
from pages.page_object import PageObject


class HomePage(PageObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.btn_next = "br.com.brmalls.customer.amazonasshopping:id/buttonNext"
        self.btn_begin = "br.com.brmalls.customer.amazonasshopping:id/customButtonLoadingText"
        self.btn_skip = "br.com.brmalls.customer.amazonasshopping:id/btSkip"
        self.welcome_message = "//android.widget.TextView[@text=\"Olá, visitante.\"]"

    def open_as_guest(self):
        self.find_element(AppiumBy.ID, self.btn_next).click()
        self.find_element(AppiumBy.ID, self.btn_next).click()
        self.find_element(AppiumBy.ID, self.btn_begin).click()
        return self.find_element(AppiumBy.XPATH, self.welcome_message).text

    def skip_splashscreen(self):
        pass
        # self.my_find_element(AppiumBy.ID, self.btn_pular_splashscreen).click()




