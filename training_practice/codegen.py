import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_role("textbox", name="email@example.com").click()
    page.get_by_role("textbox", name="email@example.com").fill("bhuvana.k@gmail.com")
    page.get_by_role("textbox", name="email@example.com").press("Tab")
    page.get_by_role("textbox", name="enter your passsword").fill("Test@12345")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name=" Add To Cart").nth(2).click()
    page.get_by_role("button", name=" Add To Cart").nth(2).click()
    page.get_by_role("button", name="   Cart").click()
    page.get_by_role("button", name="Checkout❯").click()
    page.get_by_role("textbox", name="Select Country").click()
    page.get_by_role("textbox", name="Select Country").click()
    page.get_by_role("textbox", name="Select Country").fill("indi")
    page.get_by_role("button", name=" India").click()
    page.get_by_role("textbox").nth(2).click()
    page.get_by_role("textbox").nth(2).fill("Bhuvana")
    page.locator(".actions").click()
    page.get_by_text("Place Order").click()
    page.get_by_text("Orders History Page").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
