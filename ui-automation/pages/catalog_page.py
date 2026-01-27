from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CatalogPage:
    URL = "https://cafedaria.com/catalog"

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def open(self):
        self.browser.get(self.URL)

    def add_first_product_to_cart(self):
        """Добавляет первый товар в корзину"""
        # Ждем, пока хотя бы одна кнопка "Add to Cart" станет кликабельной
        add_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.js-add-to-cart"))
        )
        add_button.click()
        # Даем странице обновиться
        time.sleep(1)

    def add_multiple_products_to_cart(self, count=2):
        """Добавляет несколько товаров в корзину"""
        for i in range(count):
            try:
                # Ждем и находим кнопку "Add to Cart" каждый раз заново
                add_button = self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.js-add-to-cart"))
                )
                add_button.click()
                # Даем странице обновиться после клика
                time.sleep(1)
            except Exception as e:
                print(f"Не удалось добавить товар #{i+1}: {e}")
                break
