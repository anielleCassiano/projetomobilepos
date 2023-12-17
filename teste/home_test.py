import unittest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from pages.home_page import HomePage


class SplashScreenTest(unittest.TestCase):

    def setUp(self) -> None:
        desired_capabilities = dict(
            {
                "platformName": "Android",
                "appium:automationName": "UiAutomator2",
                "appium:appPackage": "br.com.brmalls.customer.amazonasshopping",
                "appium:appActivity": "br.com.brmalls.customer.launcher.LauncherActivity",
                "appium:ensureWebviewsHavePages": True,
                "appium:nativeWebScreenshot": True,
                "appium:newCommandTimeout": 3600,
                "appium:connectHardwareKeyboard": True,
                "appium:autoGrantPermissions": True
            }
        )
        options = AppiumOptions()
        options.load_capabilities(desired_capabilities)
        self.driver = webdriver.Remote(command_executor="http://localhost:4723", options=options)
        self.home_page = HomePage(self.driver)

    def test_check_welcome_message_as_guest(self):
        welcome_message = self.home_page.open_as_guest()
        assert welcome_message == "Olá, visitante."

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
