from playwright.sync_api import Page,expect
import time

def test_keyboardcontrol(page: Page):
    page.goto("https://www.selenium.dev/selenium/web/web-form.html")
    page.locator("#my-text-id").click()
    page.keyboard.type("testuser")
    page.keyboard.press("Tab")
    page.keyboard.type("Password@1")
    page.keyboard.press("Tab")
    page.keyboard.type("To Test Keyboard Control")
    page.keyboard.press("Tab")
    time.sleep(5)

