import page

from pages.base_page import BasePage
class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.username = page.locator("input[name='username']")
        self.password = page.locator("input[name='password']")
        self.login_btn = page.locator("button[type='submit']")


    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()