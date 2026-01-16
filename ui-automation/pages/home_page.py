from selenium.webdriver.common.by import By

class HomePage:
    URL = "https://cafedaria.com/"

    MENU_LINK = (By.LINK_TEXT, "Menu")
    BOOK_TABLE_BUTTON = (By.LINK_TEXT, "Book a Table")
    ADDRESS_LINK = (By.LINK_TEXT, "2130 Fulton Street, San Diego, CA 94117-1080 USA")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def click_menu(self):
        self.driver.find_element(*self.MENU_LINK).click()

    def click_book_table(self):
        self.driver.find_element(*self.BOOK_TABLE_BUTTON).click()

    def click_address(self):
        self.driver.find_element(*self.ADDRESS_LINK).click()
