import re
import time
from operator import contains

from playwright.sync_api import expect
from pytest_bdd import given, when, then
from PageObject.login_page import LoginPage

@given("user is on the login page")
def open_login_page(page):
    page.goto("https://rahulshettyacademy.com/client")

@when("user enters valid credentials")
def enter_credentials(page):
    login = LoginPage(page)
    login.login("bhuvana.k@gmail.com", "Test@12345")
    time.sleep(5)

@then("user should be logged in successfully")
def verify_login(page):
    expect(page).to_have_url(re.compile("dashboard"))