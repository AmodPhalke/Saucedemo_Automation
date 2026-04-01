from playwright.sync_api import Page, sync_playwright, expect
from pages.cart_page import CartPage
import pytest

def test_sort_functionality(logged_in_page):
    cart_page = CartPage(logged_in_page)
    cart_page.dropdown.click()
    original_prices = cart_page.check_price()
    cart_page.dropdown.select_option("Price (low to high)")
    sorted_prices = cart_page.check_price()
    assert sorted_prices == sorted(original_prices)

