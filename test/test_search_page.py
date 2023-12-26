import unittest

from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.welcome_page import WelcomePage
from test.conftest import get_driver


class SearchPageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = get_driver()
        self.welcome_page = WelcomePage(driver=self.driver)
        self.home_page = HomePage(driver=self.driver)
        self.search_page = SearchPage(driver=self.driver)

    def test_store_found(self):
        store = "Ba"
        self.welcome_page.skip_welcome()
        self.home_page.accept_cookies()
        self.home_page.open_our_stores_menu()
        message = self.search_page.get_page()
        assert message == "Nossas Lojas"
        stories_found = self.search_page.search_store(store)
        for item in stories_found[0::3]:
            assert store.casefold() in item.casefold()

    def test_store_not_found(self):
        self.welcome_page.skip_welcome()
        self.home_page.accept_cookies()
        self.home_page.open_our_stores_menu()
        message = self.search_page.get_page()
        assert message == "Nossas Lojas"
        stories_found = self.search_page.search_store("Nenhuma loja")
        assert stories_found[0] == "Ops! Nenhuma loja encontrada."

    def tearDown(self):
        self.driver.quit()
