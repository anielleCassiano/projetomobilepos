from appium.webdriver.common.appiumby import AppiumBy

from pages.page_object import PageObject


class MoviesPage(PageObject):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.id_movies = "itemTextTitle"
        self.id_movie_exhibition_days = "itemMovieDateDayOfWeek"

    def get_available_movies(self):
        movies: set[str] = set()
        available_movies = self.find_elements(AppiumBy.ID, self.id_movies)

        for movie in available_movies:
            movies.add(movie.text)

        return movies

    def check_movie_exhibition(self):
        movie_names: list[str] = []
        self.find_elements(AppiumBy.ID, self.id_movies)[0].click()
        for name in self.find_elements(AppiumBy.ID, self.id_movie_exhibition_days):
            movie_names.append(name.text)

        return movie_names
