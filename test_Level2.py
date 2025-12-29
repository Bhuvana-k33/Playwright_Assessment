from playwright.sync_api import Page,expect
import time

def test_doubleclick(page: Page):
    page.goto("https://demoqa.com/buttons")
    page.locator("#doubleClickBtn").dblclick()
    expect(page.locator("#doubleClickMessage")) \
        .to_have_text("You have done a double click")

def test_rightclick(page: Page):
    page.goto("https://demoqa.com/buttons")
    page.locator("#rightClickBtn").click(button="right")
    expect(page.locator("#rightClickMessage")) \
        .to_have_text("You have done a right click")

def test_click(page: Page):
    page.goto("https://demoqa.com/buttons")
    box = page.get_by_role("button", name="Click Me").nth(0).bounding_box()

    page.mouse.move(
        box["x"] + box["width"] / 2,
        box["y"] + box["height"] / 2
    )

    page.mouse.click(
        box["x"] + box["width"] / 2,
        box["y"] + box["height"] / 2
    )