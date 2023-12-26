from appium import webdriver
from appium.options.common.base import AppiumOptions


def get_driver() -> webdriver:
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
            "appium:autoGrantPermissions": True,
        }
    )
    options = AppiumOptions()
    options.load_capabilities(desired_capabilities)
    driver = webdriver.Remote(command_executor="http://localhost:4723", options=options)
    return driver

