import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from utils import config
import pytest_bdd

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=50)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context(
        no_viewport=True,
        timezone_id="Europe/London"         # maximizes the browser window
    )
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
   # page.close()

@pytest.fixture
def logged_in_page(page):
    """Logs in and returns a page ready for testing post-login."""
    login = LoginPage(page)
    login.goto(config.BASE_URL)
    login.login(config.USERNAME, config.PASSWORD)
    return page