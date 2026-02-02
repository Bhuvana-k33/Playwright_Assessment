from pathlib import Path

from playwright.sync_api import expect

from pages.base_page import BasePage

class Dependents(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.my_info_menu = page.get_by_role("link", name="My Info")
        self.dependents_tab = page.get_by_role("link", name="Dependents")
        self.add = page.get_by_role("button", name="Add").nth(0)
        self.name= page.get_by_role("textbox").nth(1)
        self.relationshipdropdown=page.locator(".oxd-select-text-input")
        self.date=page.get_by_placeholder("yyyy-dd-mm")
        self.savebtn= page.get_by_role("button", name="Save")
        self.addbtn = page.get_by_role("button", name="Add").nth(1)
        self.addattachment = page.get_by_role("button", name="Add").nth(1)
        self.browse = page.get_by_text("Browse")
        self.saveimg = page.locator("//button[@type='submit']").nth(1)
        self.delete_btn=page.locator("i.bi-trash")
        self.yes_btn=page.get_by_role("button", name="Yes, Delete")

    def open(self):
            self.my_info_menu.click()
            self.dependents_tab.click()

    def add_dependents(self, contact):
            self.page.locator(".oxd-form-loader").wait_for(state="hidden")
            self.add.click()
            self.name.click()
            self.name.fill(contact["name"])
            # self.name.press("Tab")
            self.relationshipdropdown.click()
            self.page.get_by_role("option",name=contact["relationship"]).click()
            # self.relationship.press("Tab")
            self.date.fill(contact["date_of_birth"])
            self.savebtn.click()

    def delete_dependents(self):
        rows = self.page.get_by_role("cell",name='Mattew')

        # Wait until at least one row is visible
        expect(rows.first).to_be_visible(timeout=10000)

        row = rows.first
        row.hover()  # REQUIRED in OrangeHRM

        # Click delete icon
        row.locator("button:has(i.bi-trash)").click()

        # Confirm delete
        self.page.get_by_role("button", name="Yes, Delete").click()

    def add_attachments(self):
            self.addattachment.click()
            self.browse.click()
            # self.choosefile.click()
            file_path = Path(__file__).parent.parent / "test_data" / "sizeless_1MB.jpeg"
            self.page.set_input_files("input[type='file']", str(file_path))
            self.saveimg.click()