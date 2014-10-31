from tests.helpers.base_component import BaseComponent
__author__ = 'PunkBASSter'

class SearchResults(BaseComponent):

    selectors = {
        'self': 'searchsummary', #class name
        'body': '.body',
    }

    @property
    def count(self):
        return self.driver.find_element_by_class_name(self.selectors['self']).text

    @property
    def header_exists(self):
        return self.driver.find_element_by_class_name(self.selectors['self']).is_displayed()

    @property
    def body_exists(self):
        return self.driver.find_element_by_css_selector(self.selectors['body']).is_displayed()