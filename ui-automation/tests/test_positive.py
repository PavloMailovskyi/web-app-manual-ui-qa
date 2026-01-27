import pytest
from pages.home_page import HomePage
from pages.catalog_page import CatalogPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_home_page(browser):
    home = HomePage(browser)
    home.open()
    # Проверяем URL
    assert browser.current_url == HomePage.URL, "Not on home page"
    # Проверяем, что шапка видна
    header = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "header.page-header"))
    )
    assert header.is_displayed(), "Header is not visible on home page"

def test_navigate_to_catalog(browser):
    home = HomePage(browser)
    home.open()
    home.click_menu()
    WebDriverWait(browser, 5).until(lambda d: "/catalog" in d.current_url)
    assert "/catalog" in browser.current_url, "Navigation to catalog page failed"

def test_add_product_to_cart(browser):
    catalog = CatalogPage(browser)
    catalog.open()
    assert "/catalog" in browser.current_url, "Not on catalog page"
    catalog.add_first_product_to_cart()

def test_add_multiple_products_to_cart(browser):
    catalog = CatalogPage(browser)
    catalog.open()
    assert "/catalog" in browser.current_url, "Not on catalog page"
    catalog.add_multiple_products_to_cart(count=2)

