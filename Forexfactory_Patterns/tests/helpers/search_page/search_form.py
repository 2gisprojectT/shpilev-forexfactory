#-*- coding:UTF-8 -*-
__author__ = 'PunkBASSter'

from tests.helpers.base_component import BaseComponent

class SearchForm(BaseComponent):

    selectors = {
        'self': 'searchform',  #class name
        'input': 'searchQueryText',      #id
        'submit': 'searchSubmit', #class name
    }

    def search(self, query):
        elem = self.driver.find_element_by_id(self.selectors['input'])
        elem.clear()
        elem.send_keys(query)
        self.driver.find_element_by_class_name(self.selectors['submit']).click()