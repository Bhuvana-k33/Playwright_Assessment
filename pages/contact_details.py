import re

from playwright.sync_api import expect

from pages.base_page import BasePage


class ContactDetails(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.my_info_menu = page.get_by_role("link", name="My Info")
        self.contact_details_tab = page.get_by_role("link", name="Contact Details")
        self.street1 = page.get_by_role("textbox").nth(1)
        self.street2 = page.get_by_role("textbox").nth(2)
        self.city    = page.get_by_role("textbox").nth(3)
        self.save    = page.get_by_role("button", name="Save")
        self.toast_container = page.locator(".oxd-toast-container")
        self.toast_message = page.locator(".oxd-toast-container .oxd-toast-content")

    def open(self):
        self.my_info_menu.click()
        self.contact_details_tab.click()

    def view_contactdetails(self):
        expect(self.page).to_have_url(re.compile("contactDetails"))

    def edit_contactdetails(self):
        self.street1.click()
        self.street1.fill("Test Street 1")
        self.street1.press("Tab")
        self.street2.fill("Test Street 2")
        self.street2.press("Tab")
        self.city.fill("Test City")
        self.city.press("Tab")
        self.save.click()

    def verify_success_message(self, expected_text="SuccessSuccessfully Updated"):
        expect(self.toast_container).to_be_visible(timeout=5000)
        expect(self.toast_message).to_have_text(expected_text, timeout=5000)