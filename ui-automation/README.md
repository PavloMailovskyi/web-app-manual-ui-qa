# UI Automation Tests

This module contains UI automation tests for the Cafe Daria website.

## Tech Stack
- Python
- Selenium WebDriver
- PyTest
- webdriver-manager

## Project Structure
ui-automation/
- tests/ — UI test cases
- conftest.py — test configuration and fixtures
- requirements.txt — project dependencies

## Test Coverage
Automated tests are based on previously created manual test cases and focus on stable and critical UI functionality:

- Smoke testing
- Navigation validation
- Internal and external links verification
- Basic UI interactions (clickability and page load)

Unstable functionality (e.g. server-side errors such as 504) is covered by bug reports and intentionally excluded from UI automation.

## How to Run Tests

1. Install dependencies (pip install -r requirements.txt)
2. Run tests


## Notes
- Tests are designed for smoke and regression purposes
- Automation scope is aligned with the test plan
- Cross-browser and mobile testing can be extended in future
