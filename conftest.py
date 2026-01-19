from datetime import datetime
import os

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def set_up():
    print("Browser Setup")
    yield
    print("Browser Teardown")

def pytest_configure(config):
    reports_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(reports_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"report_{timestamp}.html"

    config.option.htmlpath = os.path.join(reports_dir, report_file)

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()
