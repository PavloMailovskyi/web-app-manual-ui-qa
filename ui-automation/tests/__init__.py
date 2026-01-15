from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import pytest




class TestGettop:
    browser = None


    def setup_method(self):
        # Install and start the browser
        driver_path = ChromeDriverManager().install()
        self.browser = webdriver.Chrome(service=Service(driver_path))


    def test_header_link(self):

        # Click laptops link
        self.browser.get('https://gettop.us/')
        self.browser.find_element(By.XPATH, "//a[@class='nav-top-link' and text()='Laptops']").click()

        #Verify correct page opens:
        expected_result = 'HOME / LAPTOP'
        actual_result = self.browser.find_element(By.XPATH,"//nav[@class='woocommerce-breadcrumb breadcrumbs uppercase']").text
        assert actual_result == expected_result

    @pytest.mark.parametrize('category', ['laptop', 'tablet', 'accessories'])
    def test_cart_link(self, category):

        # Add the laptop into the cart
        self.browser.get(f'https://gettop.us/product-category/{category}/')
        self.browser.find_element(By.XPATH, "//p[@class='name product-title']").click()

        # Store product name and click add to cart
        product_name = self.browser.find_element(By.XPATH, "//h1[contains(@class, 'product_title entry-title')]").text
        self.browser.find_element(By.XPATH, "//button[@class='single_add_to_cart_button button alt']").click()


        # Verify correct product in the cart:
        self.browser.find_element(By.XPATH, "//span[@class='cart-icon image-icon']").click()
        cart_product_name = self.browser.find_element(By.XPATH, "//td[@class='product-name']").text

        assert product_name == cart_product_name


    def test_product_search(self):
        # Search for chromebook
        self.browser.get('https://gettop.us/')
        self.browser.find_element(By.XPATH, "//a[@aria-label='Search']").click()
        self.browser.find_element(By.ID, 'woocommerce-product-search-field-0').send_keys('chromebook', Keys.ENTER)

        # Verify search results are shown
        expected_text = 'HOME / SHOP / SEARCH RESULTS FOR “CHROMEBOOK”'
        actual_text = self.browser.find_element(By.XPATH, "//nav[contains(@class, 'breadcrumb')]").text
        assert actual_text == expected_text

        expected_product = 'Chromebook'
        actual_product_title = self.browser.find_element(By.XPATH, "//p[@class='name product-title']").text
        assert expected_product in actual_product_title

    def teardown_method(self):
        self.browser.quit()