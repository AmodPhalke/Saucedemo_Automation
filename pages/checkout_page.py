from playwright.sync_api import Page, sync_playwright
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.checkout_button = page.get_by_text("Checkout")
        self.first_name_field = page.get_by_placeholder("First Name")
        self.last_name_field = page.get_by_placeholder("Last Name")
        self.zipcode_field = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_text("Continue")
        self.error_message = page.locator("[data-test='error']")

    def checkout_process(self, first_name: str, last_name: str, zip_code: str):
        self.click(self.checkout_button)
        #self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.zipcode_field.fill(zip_code)
        self.click(self.continue_button)





