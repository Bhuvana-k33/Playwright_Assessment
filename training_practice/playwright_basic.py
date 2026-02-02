from playwright.sync_api import expect

def test_basic(page):
    page.goto("https://example.com")
    expect(page).to_have_title("Example Domain")
    expect(page.locator("//h1[text()='Example Domain']")).to_have_text('Example Domain')

def test_verify_text(page):
    page.goto("https://example.com")
    expect(page.locator("p", has_text="This domain is for use in documentation examples without needing permission. Avoid use in operations.")).to_be_visible()

def test_negative_case(page):
    page.goto("https://example.com")
    expect(page).to_have_title("Test Domain")
