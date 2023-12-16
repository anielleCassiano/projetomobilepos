import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from pages.PageObject import PageObject


class SplashScreenPage():

    btn_proximo = "br.com.brmalls.customer.amazonasshopping:id/buttonNext"
    btn_comecar = "br.com.brmalls.customer.amazonasshopping:id/customButtonLoadingText"
    titulo_home = "//android.widget.TextView[@text=\"Olá, visitante.\"]"
    btn_pular_splashScreen = "br.com.brmalls.customer.amazonasshopping:id/btSkip"

    def __init__(self):
        self.page = PageObject()
        self.driver = self.page.driver
        super(SplashScreenPage, self).__init__()

    def acessar_SplashScreen(self):
        self.page.myFindElement(AppiumBy.ID,self.btn_proximo).click()
        self.page.myFindElement(AppiumBy.ID, self.btn_proximo).click()
        self.page.myFindElement(AppiumBy.ID, self.btn_comecar).click()
        self.tituloPage = self.page.myFindElement(AppiumBy.XPATH, self.titulo_home).text
        return self.tituloPage

    def pular_SplashScreen(self):
        self.page.myFindElement(AppiumBy.ID, self.btn_pular_splashScreen).click()




