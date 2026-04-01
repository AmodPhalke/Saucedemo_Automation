from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def click(self, locator):
        locator.click()

    def fill(self, locator, value: str):
        locator.fill(value)

    def count(self, locator):
        return locator.count()

    def get_text(self, locator):
        return self.page.inner_text(locator)

