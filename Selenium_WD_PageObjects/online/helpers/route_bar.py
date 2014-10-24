__author__ = 'PunkBASSter'

from online.helpers.base_component import BaseComponent


class RouteBar(BaseComponent):

    selectors = {
        'self': '.searchBar__tabs .searchBar__tab.searchBar__rsTab',
        'inp_from': '.searchBar__form .searchBar__textfield._from .suggest__input',
        'inp_to': '.searchBar__form .searchBar__textfield._to .suggest__input',
        'submit': '.searchBar__submit._refbook',
    }

    def search(self, inpfrom, inpto):
        self.driver.find_element_by_css_selector(self.selectors['self']).click()
        self.driver.find_element_by_css_selector(self.selectors['inp_from']).send_keys(inpfrom)
        self.driver.find_element_by_css_selector(self.selectors['inp_to']).send_keys(inpto)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()