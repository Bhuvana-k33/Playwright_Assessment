import time

from playwright.sync_api import sync_playwright


def test_login_and_save_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        page = context.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        page.fill("//input[@name='username']", "Admin")
        page.fill("//input[@name='password']", "admin123")
        page.click("//button[@type='submit']")

       # page.wait_for_url("**/dashboard")

        # Save authenticated state
        #context.storage_state(path="auth_state.json")
        browser.close()