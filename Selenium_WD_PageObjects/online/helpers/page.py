class Page():
    def __init__(self, driver):

        self.driver = driver
        self._search_bar = None
        self._search_result = None
        self._route_bar = None
        self._route_result = None
        self._share_link = None

    @property
    def search_bar(self):
        from online.helpers.search_bar import SearchBar

        if self._search_bar is None:
            self._search_bar = SearchBar(self.driver, self.driver.find_element_by_css_selector(SearchBar.selectors['self']))
        return self._search_bar

    @property
    def search_result(self):
        from online.helpers.search_result import SearchResult

        if self._search_result is None:
            self._search_result = SearchResult(self.driver, self.driver.find_element_by_css_selector(SearchResult.selectors['self']))
        return self._search_result

    @property
    def route_bar(self):
        from online.helpers.route_bar import RouteBar

        if self._route_bar is None:
            self._route_bar = RouteBar(self.driver, self.driver.find_element_by_css_selector(RouteBar.selectors['self']))
        return self._route_bar

    @property
    def route_result(self):
        from online.helpers.route_result import RouteResult

        if self._route_result is None:
            self._route_result = RouteResult(self.driver, self.driver.find_element_by_css_selector(RouteResult.selectors['self']))
        return self._route_result

    @property
    def share_link(self):
        from online.helpers.share_link import ShareLink

        if self._share_link is None:
            self._share_link = ShareLink(self.driver, self.driver.find_element_by_css_selector(ShareLink.selectors['self']))
        return self._share_link

    def open(self, url):
        self.driver.get(url)

