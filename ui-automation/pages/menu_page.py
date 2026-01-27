from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenuPage:
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains(., 'Add')]")
    CART_COUNT = (By.CLASS_NAME, "cart-count")

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def add_first_product_to_cart(self):
        buttons = self.wait.until(
            EC.presence_of_all_elements_located(self.ADD_TO_CART_BUTTONS)
        )
        buttons[0].click()
        self.wait.until(EC.visibility_of_element_located(self.CART_COUNT))
