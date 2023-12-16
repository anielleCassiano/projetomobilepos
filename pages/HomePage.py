from appium.webdriver.common.appiumby import AppiumBy

from pages.PageObject import PageObject


class HomePage():
    titulo_home = "//android.widget.TextView[@text=\"Olá, visitante.\"]"
    btn_alerta = "//android.widget.TextView[@text=\"Aceitar e continuar\"]"
    btn_verMais = "//android.widget.TextView[@text=\"ver mais\"]"

    def __init__(self):
        self.page = PageObject()
        self.driver = self.page.driver
        super(HomePage, self).__init__()

    def verificar_titulo_home(self):
        self.title = self.page.myFindElement(AppiumBy.ID, self.titulo_home).text
        return self.title



