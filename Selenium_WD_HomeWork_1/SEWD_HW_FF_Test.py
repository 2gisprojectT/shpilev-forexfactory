__author__ = 'PunkBASSter'

from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#--------------------------------------------------------

class SeleniumTest(TestCase):

    #test of login and logout positive
    def test_login_positive(self):
        drv = webdriver.Firefox()
        drv.get("http://www.forexfactory.com/")
        assert "Forex Factory" in drv.title
        #logging in
        drv.find_element_by_css_selector(".login > a:nth-child(1) > span:nth-child(1)").click()
        #typing username
        drv.find_element_by_name("vb_login_username").send_keys("PunkBASSter")
        #typing password + Enter
        elem = drv.find_element_by_name("vb_login_password")
        elem.send_keys("testpassword123")
        elem.send_keys(Keys.RETURN)
        #checking if login is successful
        assert "PunkBASSter's" in drv.title
        #logging out
        drv.find_element_by_css_selector(".logout > a:nth-child(1) > span:nth-child(1)").click()
        assert "Forex Factory" in drv.title
        drv.close()

    def test_login_negative(self):
        drv = webdriver.Firefox()
        drv.get("http://www.forexfactory.com/")
        assert "Forex Factory" in drv.title
        #logging in
        drv.find_element_by_css_selector(".login > a:nth-child(1) > span:nth-child(1)").click()
        #typing username
        drv.find_element_by_name("vb_login_username").send_keys("Ololo")
        #typing password + Enter
        elem = drv.find_element_by_name("vb_login_password")
        elem.send_keys("qweasd123")
        elem.send_keys(Keys.RETURN)
        #checking if login failed and processed correctly
        assert "http://www.forexfactory.com/login.php?do=login" in drv.current_url
        drv.close()

if __name__ == '__main__':
    unittest.main()
