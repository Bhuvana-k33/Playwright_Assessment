import re
import json
from pathlib import Path

import page
import row
from playwright.sync_api import expect

from pages.base_page import BasePage

class EmergencyContact(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.my_info_menu = page.get_by_role("link", name="My Info")
        self.emergency_contact_tab = page.get_by_role("link", name="Emergency Contacts")
        self.addbtn=page.get_by_role("button",name="Add").nth(0)
        self.name=page.get_by_role("textbox").nth(1)
        self.relationship=page.get_by_role("textbox").nth(2)
        self.telephone=page.get_by_role("textbox").nth(3)
        self.savebtn=page.get_by_role("button",name="Save")
        #self.deletebtn= page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(0)
        self.yesbtn=page.locator("button:has(i.bi-trash)")
        self.addattachment=page.get_by_role("button",name="Add").nth(1)
        self.browse=page.get_by_text("Browse")
        #self.choosefile= page.get_by_role("button", name="Choose File")
        self.saveimg= page.locator("//button[@type='submit']").nth(1)

    def open(self):
        self.my_info_menu.click()
        self.emergency_contact_tab.click()

    def add_emergency_contact(self,contact):
            self.page.locator(".oxd-form-loader").wait_for(state="hidden")
            self.addbtn.click()
            self.name.click()
            self.name.fill(contact["name"])
           # self.name.press("Tab")
            self.relationship.fill(contact["relationship"])
           # self.relationship.press("Tab")
            self.telephone.fill(contact["home_phone"])
            self.savebtn.click()

    def delete_emergency_contact(self):
       # row=self.page.locator("tr", has_text=contact["name"])

        #self.yesbtn.click()

        #row = self.page.locator("tr", has_text=contact["name"])

    # 2️⃣ Click delete icon inside that row
       # row.locator("button:has(i.bi-trash)").first.click()
       row = self.page.locator("div.oxd-table-row").first
       row.hover()
       row.locator("i.bi-trash").click()
       #self.delete_btn.click()
       self.yesbtn.click()

    def add_attachments(self):
            self.addattachment.click()
            self.browse.click()
            #self.choosefile.click()
            file_path = Path(__file__).parent.parent / "test_data" /"sizeless_1MB.jpeg"
            self.page.set_input_files("input[type='file']", str(file_path))
            self.saveimg.click()