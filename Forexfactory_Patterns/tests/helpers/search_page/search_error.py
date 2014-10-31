#-*- coding:UTF-8 -*-
__author__ = 'PunkBASSter'

from tests.helpers.base_component import BaseComponent

class SearchError(BaseComponent):

    selectors = {
        'self': '.error',
        'query': '.title > strong:nth-child(1)'
    }

    @property
    def error_exists(self):
        return self.driver.find_element_by_css_selector(self.selectors['self']).is_displayed()

    @property
    def query(self):
        return self.driver.find_element_by_css_selector(self.selectors['query']).text