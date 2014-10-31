#-*- coding:UTF-8 -*-
__author__ = 'PunkBASSter'

from tests.helpers.base_component import BaseComponent

class QuickSearch(BaseComponent):

    selectors = {
        'self': 'quickSearch',  #class name
        'input': 'search',      #name
        'submit': '.submit', #link text
    }

    def search(self, query):
        self.driver.find_element_by_name(self.selectors['input']).send_keys(query)
        self.driver.find_element_by_css_selector(self.selectors['submit']).click()