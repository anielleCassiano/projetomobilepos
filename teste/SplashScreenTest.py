import unittest
from pages.SplashScreenPage import SplashScreenPage


class SplashScreenTest(unittest.TestCase):
    def setUp(self) -> None:
        self.texto_titulo = 'Olá, visitante.'
        self.ssp = SplashScreenPage()

    def test_acessar_home_app(self):
        self.titulo = self.ssp.acessar_SplashScreen()
        assert self.titulo == self.texto_titulo
        self.ssp.page.close()

'''
if __name__ == '__main__':
    unittest.main()
'''


