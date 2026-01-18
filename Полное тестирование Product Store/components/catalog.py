from controls.product import Product


class Catalog:
    def __init__(self, driver):
        self.driver = driver

    def wrapper(self):
        return self.driver.locator('//div[@class = "col-lg-9"]')

    def get_product_by_title(self, title):
        return Product(self.driver, title)
