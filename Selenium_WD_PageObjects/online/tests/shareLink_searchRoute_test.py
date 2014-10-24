#-*- coding:UTF-8 -*-
__author__ = 'PunkBASSter'

from unittest import TestCase
import unittest
from selenium import webdriver
from online.helpers.page import Page

class Share_Route_Test(TestCase):

    def test_share(self):
        driver = webdriver.Firefox()
        page = Page(driver)
        page.open("http://2gis.ru")
        search_string = u'кафе'
        page.search_bar.search(search_string)
        url = page.share_link.share()
        driver.implicitly_wait(10)
        page.open(url)
        self.assertEqual(search_string, page.search_bar.getQuery(), "Something went wrong with sharing a link")
        driver.close()

    def test_route(self):
        driver = webdriver.Firefox()
        page = Page(driver)
        page.open("http://2gis.ru")
        page.route_bar.search(u'Площадь Маркса', u'Стадион Сибирь')
        driver.implicitly_wait(10) #doesnt work otherwise
        self.assertTrue(page.route_result.exists, "No routes found")
        self.assertLess("", page.route_result.time, "No routes found")
        driver.close()

if __name__ == '__main__':
    unittest.main()