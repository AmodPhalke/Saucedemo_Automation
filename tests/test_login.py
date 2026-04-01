import pytest
import re
from pages.login_page import LoginPage
from playwright.sync_api import expect
from config import constants

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate(constants.base_url)
    login_page.perform_login(constants.valid_username, constants.valid_password)
    assert "inventory" in page.url
    expect(page.get_by_text("Products")).to_be_visible()
    expect(page.locator(".shopping_cart_link")).to_be_visible()

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.navigate(constants.base_url)
    login_page.perform_login(constants.invalid_username, constants.invalid_password)
    expect(page.get_by_text("Epic sadface: Username and password do not match any user in this service")).to_be_visible()
    expect(page.get_by_text("Epic sadface: Username and password do not match any user in this service")).to_contain_text("do not match")


