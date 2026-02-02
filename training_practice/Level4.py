import time

from playwright.sync_api import Page,expect


def test_iframe(page: Page):
    content="I rule the frames!"
    page.goto("https://the-internet.herokuapp.com/iframe")
    frame = page.frame_locator("#mce_0_ifr")
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.locator("//div[@class='tox-icon']").click()
    time.sleep(5)
    frame.locator("#tinymce").clear()
    frame.locator("#tinymce").fill(content)

    expect(frame.locator("#tinymce")).to_have_text(content)

