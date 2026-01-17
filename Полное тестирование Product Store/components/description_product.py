from controls.button_add_cart import ButtonAddCart


class Description:
    def __init__(self, driver):
        self.driver = driver

    def wrapper(self):
        return self.driver.locator('//div[@id = "tbodyid"]')

    def get_button_add_cart(self):
        return ButtonAddCart(self.driver)
