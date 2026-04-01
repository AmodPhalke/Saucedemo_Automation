from playwright.sync_api import Page, sync_playwright, expect
from pages.base_page import BasePage
from config import constants

class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.username_field = page.get_by_placeholder("Username")
        self.password_field = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

    def perform_login(self, username : str, password : str):
        self.fill(self.username_field, username)
        self.fill(self.password_field, password)
        self.click(self.login_button)




