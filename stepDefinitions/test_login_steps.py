import re
import time

from playwright.sync_api import expect
from pytest_bdd import given, when, then, parsers
from pages import login_page
from pages.login_page import LoginPage



@given("user is on the login page")
def open_login_page(page):
    page.goto("https://opensource-demo.orangehrmlive.com")

# Note: In the Feature file use: When user enters username "<username>" and password "<password>"
@when(parsers.parse('user enters username "{username}" and password "{password}"'))
def enter_credentials(page, username, password):
    LoginPage(page).login(username, password)

# 3. Step for Scenario 1
@then("user should be logged in successfully")
def verify_login_success(page):
    expect(page).to_have_url(re.compile("dashboard"))

# 4. Step for Scenario 2
@then("login should fail with an error message")
def verify_login_failure(page):
    # OrangeHRM usually shows 'Invalid credentials' for failed logins
    expect(page.get_by_text("Invalid credentials")).to_be_visible()