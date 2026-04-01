import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from config import constants
import os

@pytest.fixture
def page():
    is_ci = os.getenv("CI") == "true"  # GitHub Actions sets this automatically
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=is_ci,  # True in CI, False on your local machine
            slow_mo=0 if is_ci else 800  # No slow-mo in CI, slow-mo locally
        )
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)
    login_page.navigate(constants.base_url)
    login_page.perform_login(constants.valid_username, constants.valid_password)
    return page
