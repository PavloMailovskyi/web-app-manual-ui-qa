from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    EMAIL_INPUT = (By.NAME, "email")

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def fill_email(self, email: str):
        el = self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))
        el.clear()
        el.send_keys(email)

    def fill_invalid_email(self):
        self.fill_email("invalid-email")

    def submit_form(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
