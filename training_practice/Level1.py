from playwright.sync_api import Page,expect
import time

def test_accept_alert(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Click for JS Alert").click()

    time.sleep(5)

def test_dismiss_alert(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Click for JS Confirm").click()

def test_AlertboxWithTextEnter(page : Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    def handle_Dialog(dialog):
        dialog.accept("Test Playwright")

    page.on("dialog", handle_Dialog)
    page.get_by_role("button", name="Click for JS Prompt").click()

    expect(page.locator("#result")).to_have_text("You entered: Test Playwright")
    time.sleep(5)