__author__ = 'PunkBASSter'
from online.helpers.base_component import BaseComponent

class ShareLink(BaseComponent):
    selectors = {
        'self': '.extras__btn.extras__share',
        'link': '.share__popupUrlInput'
    }

    def share(self):
        self.driver.find_element_by_css_selector(self.selectors['self']).click()
        url = self.driver.find_element_by_css_selector(self.selectors['link']).get_attribute('value')
        return url