import pytest
from pages.home_page import HomePage

def test_header_footer_visibility(browser):
    browser.get("https://cafedaria.com/")
    header = browser.find_element_by_tag_name("header")
    footer = browser.find_element_by_tag_name("footer")
    assert header.is_displayed()
    assert footer.is_displayed()

def test_book_table_scroll(browser):
    home = HomePage(browser)
    home.open()
    home.click_book_table()
    # Just check page scrolled up, no new booking page
    assert browser.execute_script("return window.pageYOffset") == 0

def test_address_link(browser):
    home = HomePage(browser)
    home.open()
    home.click_address()
    assert "contacts" in browser.current_url.lower()

def test_mobile_resolution(browser):
    browser.set_window_size(375, 667)  # iPhone 8 resolution
    browser.get("https://cafedaria.com/")
    header = browser.find_element_by_tag_name("header")
    assert header.is_displayed()

