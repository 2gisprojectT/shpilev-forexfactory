__author__ = 'PunkBASSter'

#http://www.forexfactory.com/search.php

class SearchPage():
    def __init__(self, driver):

        self.driver = driver
        self._search_form = None
        self._search_results = None
        self._search_error = None

    @property
    def search_form(self):
        from tests.helpers.search_page.search_form import SearchForm

        if self._search_form is None:
            self._search_form = SearchForm(self.driver, self.driver.find_element_by_class_name(SearchForm.selectors['self']))
        return self._search_form

    @property
    def search_results(self):
        from tests.helpers.search_page.search_results import SearchResults

        if self._search_results is None:
            self._search_results = SearchResults(self.driver, self.driver.find_element_by_class_name(SearchResults.selectors['self']))
        return self._search_results

    @property
    def search_error(self):
        from tests.helpers.search_page.search_error import SearchError

        if self._search_error is None:
            self._search_error = SearchError(self.driver, self.driver.find_element_by_css_selector(SearchError.selectors['self']))
        return self._search_error

    def open(self, url):
        self.driver.get(url)