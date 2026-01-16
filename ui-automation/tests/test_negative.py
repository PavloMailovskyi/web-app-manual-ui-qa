import pytest
from pages.checkout_page import CheckoutPage

def test_checkout_empty_form(browser):
    browser.get("https://cafedaria.com/checkout/")
    checkout = CheckoutPage(browser)
    checkout.submit_form()
    assert "required" in browser.page_source.lower()

def test_invalid_email_format(browser):
    browser.get("https://cafedaria.com/checkout/")
    checkout = CheckoutPage(browser)
    checkout.fill_invalid_email()
    checkout.submit_form()
    assert "email" in browser.page_source.lower()
