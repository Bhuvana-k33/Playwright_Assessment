class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.fill("#userEmail", username)
        self.page.fill("#userPassword", password)
        self.page.click("#login")