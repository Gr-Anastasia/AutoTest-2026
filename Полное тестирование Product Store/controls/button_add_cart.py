class ButtonAddCart:
    def __init__(self, driver):
        self.driver = driver

    def wrapper(self):
        return self.driver.get_by_role("link", name="Add to cart")