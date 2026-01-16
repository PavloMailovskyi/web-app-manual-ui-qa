import pytest
from pages.home_page import HomePage
from pages.menu_page import MenuPage

def test_open_home_page(browser):
    home = HomePage(browser)
    home.open()
    assert "Cafedaria" in browser.title

def test_navigate_to_menu(browser):
    home = HomePage(browser)
    home.open()
    home.click_menu()
    assert "menu" in browser.current_url.lower()

def test_add_product_to_cart(browser):
    home = HomePage(browser)
    home.open()
    home.click_menu()
    menu = MenuPage(browser)
    menu.add_first_product_to_cart()
    cart_count = browser.find_element_by_class_name("cart-count")
    assert int(cart_count.text) > 0

def test_add_multiple_products_to_cart(browser):
    home = HomePage(browser)
    home.open()
    home.click_menu()
    menu = MenuPage(browser)
    menu.add_first_product_to_cart()
    menu.add_first_product_to_cart()
    cart_count = browser.find_element_by_class_name("cart-count")
    assert int(cart_count.text) >= 2
