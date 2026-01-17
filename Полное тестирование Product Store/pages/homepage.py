from components.catalog import Catalog


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.demoblaze.com/index.html'

    def open(self):
        self.driver.goto(self.url)

    def get_catalog(self):
        return Catalog(self.driver)

    def product_click_by_title(self, title):
        self.get_catalog().get_product_by_title(title).wrapper().click()
