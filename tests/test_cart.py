import pytest
import re
from pages.cart_page import CartPage
from playwright.sync_api import expect
from config import constants

def test_cart_functionality(logged_in_page):
    cart_page = CartPage(logged_in_page)
    cart_page.add_products()
    expect(cart_page.badge).to_have_text("3")
    cart_page.remove_products()
    expect(cart_page.badge).to_have_text("1")