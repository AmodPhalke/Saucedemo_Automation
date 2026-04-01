import pytest
from playwright.sync_api import Page, expect, sync_playwright
from config import constants
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_process(logged_in_page):
    cart_page = CartPage(logged_in_page)
    cart_page.add_products()
    cart_page.click(cart_page.badge)

    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.checkout_process("", constants.last_name, constants.zip_code)

    expect(checkout_page.error_message).to_be_visible()
    expect(checkout_page.error_message).to_have_text("Error: First Name is required")

