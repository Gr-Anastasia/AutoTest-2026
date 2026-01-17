class Product:
    def __init__(self, driver, title):
        self.driver = driver
        self.title = title

    def wrapper(self):
        return self.driver.get_by_role("link", name=f"{self.title}")
