from playwright.sync_api import Page
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.add_to_Cart_button = page.locator("button:has-text('Add to cart')")
        self.remove_button = page.locator("button:has-text('Remove')")
        self.badge = page.locator(".shopping_cart_badge")
        self.dropdown = page.locator(".product_sort_container")
        self.prices = page.locator(".inventory_item_price")

    def add_products(self):
        self.add_to_Cart_button.nth(0).click()
        self.add_to_Cart_button.nth(1).click()
        self.add_to_Cart_button.nth(2).click()

    def remove_products(self):
        for i in range(2):
            self.remove_button.nth(0).click()

    def check_price(self):
        price_texts = self.prices.all_text_contents()
        return [float(price.replace("$", "")) for price in price_texts]
