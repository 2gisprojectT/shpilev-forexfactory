#-*- coding:UTF-8 -*-
__author__ = 'PunkBASSter'

from unittest import TestCase
import unittest

from selenium import webdriver
from unittest_data_provider import data_provider

from tests.helpers.main_page.page_main import MainPage
from tests.helpers.search_page.page_search import SearchPage


class ff_main_page_tests(TestCase):

    driver = None
    main_page = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(5)
        cls.main_page = MainPage(cls.driver)
        cls.main_page.open("http://forexfactory.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    logins_valid = lambda: (
        ("PunkBASSter", "testpassword123",),
    )

    @data_provider(logins_valid)
    def test_login_positive(self,username, password):
        self.main_page.login_form.login(username, password)
        try:
            self.assertIn(username, self.driver.title, "Wrong user data")
            self.assertIn(username, self.driver.page_source, "Wrong user data")
        except:
            self.assertIn("Sorry, you have used all of your login attempts", self.driver.page_source, "Unknown error")
        #После 5 провальных попыток авторизации с неверными данными, включается защитный таймаут 15 минут, сообщение
        #о нем выводится на отдельной странице, поэтому трай-кэтч -- чтобы тест, падал только если оба
        #ассерта провалились. В первом случае - успешная авторизация, во втором - защитный таймаут. При этом, оба случая
        #являются взаимоисключающими положительными результатами.


    logins_invalid = lambda: (
        ("BASSpunkter", "invalid_password",),
        ("invaliduser", "invalid_password",),
    )

    @data_provider(logins_invalid)
    def test_login_negative(self, username, password):
        self.main_page.login_form.login(username, password)
        self.assertNotIn(username, self.driver.title, "Unexpected error") #не зашли в лк - это правильно
        try:
            self.assertIn("Forgot your password?", self.driver.page_source, "No error page shown")
        except:
            self.assertIn("Sorry, you have used all of your login attempts", self.driver.page_source, "Unknown error")
        #После 5 провальных попыток авторизации с неверными данными, включается защитный таймаут 15 минут, сообщение
        #о нем выводится вместо формы логина, поэтому трай-кэтч -- чтобы тест, падал только если оба ассерта провалились
        #В первом случае - провал авторизации и форма входа, во втором - вместо формы входа защитный таймаут.
        #В обоих случаях имеем взаимоисключающие положительные результаты.





class ff_search_page_tests(TestCase):

    driver = None
    search_page = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(5)
        cls.search_page = SearchPage(cls.driver)
        cls.search_page.open("http://forexfactory.com/search.php")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


    queries_valid = lambda: ( #query, expected_result to be used in assert
        ("nonfarm",),
        ("oanda",),
    )


    @data_provider(queries_valid)
    def test_search_positive(self, query):
        self.search_page.search_form.search(query)
        self.assertTrue(self.search_page.search_results.header_exists, "No results for a valid query")
        self.assertTrue(self.search_page.search_results.body_exists, "No results for a valid query")

    queries_invalid = lambda: (
        ("azaza",),
        ("ololo",),
    )

    @data_provider(queries_invalid)
    def test_search_negative(self, query):
        self.search_page.search_form.search(query)
        self.assertTrue(self.search_page.search_error.error_exists, "No error message for an invalid query")
        self.assertEqual(query, self.search_page.search_error.query, "Wrong query was processed")

    @data_provider(queries_invalid)
    def test_quick_search(self, query): #Тест меню быстрого поиска - проверяем переход на страницу /search.php, используем негативный запрос
        main_page = MainPage(self.driver)
        main_page.open("http://forexfactory.com")#Переходим на главную, чтобы появился быстрый поиск
        main_page.quick_search.search(query)
        self.assertTrue(self.search_page.search_error.error_exists, "No error message for an invalid query")
        self.assertEqual(query, self.search_page.search_error.query, "Wrong query was processed")

if __name__ == '__main__':
    unittest.main()