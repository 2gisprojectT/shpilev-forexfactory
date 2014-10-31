#-*- coding:UTF-8 -*-
__author__ = 'PunkBASSter'

from tests.helpers.base_component import BaseComponent

class LoginForm(BaseComponent):

    selectors = {
        'self': '.login',
        'panel_show': '.login > a:nth-child(1) > span:nth-child(1)',
        'username': 'vb_login_username',
        'password': 'vb_login_password',
        'remember': 'login_remember',
        'login': '.loginform.active > span > form > input[type="submit"]:nth-child(7)',
    }

    def login(self, username, password):
        self.driver.find_element_by_css_selector(self.selectors['panel_show']).click()
        self.driver.find_element_by_name(self.selectors['username']).send_keys(username)
        self.driver.find_element_by_name(self.selectors['password']).send_keys(password)
        self.driver.find_element_by_id(self.selectors['remember']).__setattr__("value", 0)
        self.driver.find_element_by_css_selector(self.selectors['login']).submit()
