import re
import time
from operator import contains

from playwright.sync_api import expect
from pytest_bdd import given, when, then
from pages.login_page import LoginPage

@given("user is on the login page")
def open_login_page(page):
    def open_login_page(page):
        page.goto("https://opensource-demo.orangehrmlive.com/")
        return page

@when('user enters username "<username>" and password "<password>"')
def enter_credentials(page, username, password):
    login_page = LoginPage(page)
    login_page.login(username, password)

@then("user should be logged in successfully")
def verify_login_success(page):
    expect(page).to_have_url_contains("dashboard")