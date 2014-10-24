__author__ = 'PunkBASSter'

from online.helpers.base_component import BaseComponent


class RouteResult(BaseComponent):
    selectors = {
        'self': '#module-1-9-1-1',
        'time': '.routeResults__time'
    }

    @property
    def time(self):
        return self.driver.find_element_by_css_selector(self.selectors['time']).text

    @property
    def exists(self):
        return self.driver.find_element_by_css_selector(self.selectors['self']).is_displayed()