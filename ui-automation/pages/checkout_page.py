from selenium.webdriver.common.by import By

class CheckoutPage:
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    EMAIL_INPUT = (By.NAME, "email")

    def __init__(self, driver):
        self.driver = driver

    def submit_form(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def fill_invalid_email(self):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys("invalid-email")
