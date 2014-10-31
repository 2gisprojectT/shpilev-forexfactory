__author__ = 'PunkBASSter'

#http://www.forexfactory.com/

class MainPage():
    def __init__(self, driver):

        self.driver = driver
        self._login_form = None
        self._quick_search = None


    @property
    def login_form(self):
        from tests.helpers.main_page.login_form import LoginForm

        if self._login_form is None:
            self._login_form = LoginForm(self.driver, self.driver.find_element_by_css_selector(LoginForm.selectors['self']))
        return self._login_form

    @property
    def quick_search(self):
        from tests.helpers.main_page.quick_search import QuickSearch

        if self._quick_search is None:
            self._quick_search = QuickSearch(self.driver, self.driver.find_element_by_class_name(QuickSearch.selectors['self']))
        return self._quick_search

    def open(self, url):
        self.driver.get(url)