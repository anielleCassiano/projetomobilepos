from appium import webdriver
from appium.options.common.base import AppiumOptions
from selenium.webdriver.support.wait import WebDriverWait


class PageObject():

    def __init__(self) -> None:
        options = AppiumOptions()
        options.load_capabilities({
            "platformName": "Android",
            "appium:automationName": "UiAutomator2",
            "appium:appPackage": "br.com.brmalls.customer.amazonasshopping",
            "appium:appActivity": "br.com.brmalls.customer.launcher.LauncherActivity",
            "appium:ensureWebviewsHavePages": True,
            "appium:nativeWebScreenshot": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True
        })

        self.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    def myFindElement(self, by, value):
        return WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element(by=by, value=value))

    def close(self):
        self.driver.quit()




