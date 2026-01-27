from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_header_footer_visibility(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, 10)
    header = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "header"))
    )
    footer = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "footer"))
    )
    assert header.is_displayed()
    assert footer.is_displayed()


def test_mobile_resolution(browser, base_url):
    browser.set_window_size(375, 667)
    browser.get(base_url)

    headers = browser.find_elements(By.CLASS_NAME, "page-header")
    assert len(headers) > 0
