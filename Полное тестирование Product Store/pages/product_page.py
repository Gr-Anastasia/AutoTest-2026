from components.description_product import Description


class CartProduct:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.demoblaze.com/prod.html?idp_=6"

    def open(self):
        self.driver.goto(self.url)

    def get_description_product(self):
        return Description(self.driver)

    def product_add_to_cart_click(self):
        self.get_description_product().get_button_add_cart().wrapper().click()
