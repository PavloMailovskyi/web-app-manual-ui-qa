from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    URL = "https://cafedaria.com/"

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(self.URL)

    def click_menu(self):
        # Кнопка "Menu" ведёт на каталог
        menu_button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/catalog/']"))
        )
        menu_button.click()
