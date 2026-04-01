import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from config import constants

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=800)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)
    login_page.navigate(constants.base_url)
    login_page.perform_login(constants.valid_username, constants.valid_password)
    return page
