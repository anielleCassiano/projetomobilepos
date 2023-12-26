import unittest

from pages.home_page import HomePage
from pages.menu_page import MenuPage
from pages.movies_page import MoviesPage
from pages.welcome_page import WelcomePage
from test.conftest import get_driver


class SearchPageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = get_driver()
        self.welcome_page = WelcomePage(driver=self.driver)
        self.home_page = HomePage(driver=self.driver)
        self.menu_page = MenuPage(driver=self.driver)
        self.movies_page = MoviesPage(driver=self.driver)

    def test_check_available_movies(self):
        self.welcome_page.skip_welcome()
        self.home_page.accept_cookies()
        self.home_page.open_bottom_menu()
        self.menu_page.open_movies()
        movies = self.movies_page.get_available_movies()
        assert len(movies) > 0

    def test_check_movie_exhibition_date(self):
        week_days: list[str] = ["Hoje", "Seg", "Ter", "Qua", "Qui", "Set", "Sab", "Dom"]
        self.welcome_page.skip_welcome()
        self.home_page.accept_cookies()
        self.home_page.open_bottom_menu()
        self.menu_page.open_movies()
        exhibition_days = self.movies_page.check_movie_exhibition()
        for day in exhibition_days:
            assert day in week_days

    def tearDown(self):
        self.driver.quit()
