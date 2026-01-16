from selenium.webdriver.common.by import By

class MenuPage:
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains(text(),'Add to Cart')]")

    def __init__(self, driver):
        self.driver = driver

    def add_first_product_to_cart(self):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        buttons[0].click()
