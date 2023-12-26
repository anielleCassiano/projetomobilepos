from appium.webdriver.common.appiumby import AppiumBy

from pages.page_object import PageObject, select_locator_by_text


class SearchPage(PageObject):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.page = select_locator_by_text("Nossas Lojas")
        self.btn_search = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[2]"
        self.input_search_store = "//android.widget.EditText"
        self.search_list = "//android.widget.TextView"

    def get_page(self):
        return self.find_element(AppiumBy.XPATH, self.page).text

    def search_store(self, store):
        self.find_element(AppiumBy.XPATH, self.btn_search).click()
        self.find_element(AppiumBy.XPATH, self.input_search_store).send_keys(store)
        stories_found = self.find_elements(AppiumBy.XPATH, self.search_list)
        return [store.text for store in stories_found]
