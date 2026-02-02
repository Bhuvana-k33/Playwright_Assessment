from pathlib import Path

from playwright.sync_api import expect

from pages.base_page import BasePage

class Immigration(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.my_info_menu = page.get_by_role("link", name="My Info")
        self.immigration_tab = page.get_by_role("link", name="Immigration")
        self.add = page.get_by_role("button", name="Add").nth(0)
        self.passportnumber= page.get_by_role("textbox").nth(1)
        self.issueddate=page.get_by_placeholder("yyyy-dd-mm").nth(0)
        self.expirydate=page.get_by_placeholder("yyyy-dd-mm").nth(1)
        self.issuedbydropdown=page.locator(".oxd-select-text-input")
        self.reviewdate=page.get_by_placeholder("yyyy-dd-mm").nth(2)
        self.savebtn= page.get_by_role("button", name="Save")
        self.addbtn = page.get_by_role("button", name="Add").nth(1)
        self.addattachment = page.get_by_role("button", name="Add").nth(1)
        self.browse = page.get_by_text("Browse")
        self.saveimg = page.locator("//button[@type='submit']").nth(1)

    def open(self):
            self.my_info_menu.click()
            self.immigration_tab.click()

    def add_immigration(self, contact):
            self.page.locator(".oxd-form-loader").wait_for(state="hidden")
            self.add.click()
            self.passportnumber.click()
            self.passportnumber.fill(contact["passportnumber"])
            self.issueddate.fill(contact["issued_date"])
            self.expirydate.fill(contact["expiry_date"])
            self.issuedbydropdown.click()
            self.page.get_by_role("option", name=contact["issued_by"]).click()

            self.savebtn.click()

        #def delete_emergency_contact(self):
            # row=self.page.locator("tr", has_text=contact["name"])

            # self.yesbtn.click()

            # row = self.page.locator("tr", has_text=contact["name"])

            # 2️⃣ Click delete icon inside that row
            # row.locator("button:has(i.bi-trash)").first.click()
           # row = self.page.locator("div.oxd-table-row").first
            #row.hover()
            #row.locator("i.bi-trash").click()
            # self.delete_btn.click()
            #self.yesbtn.click()

    def add_attachments(self):
            self.addattachment.click()
            self.browse.click()
            # self.choosefile.click()
            file_path = Path(__file__).parent.parent / "test_data" / "sizeless_1MB.jpeg"
            self.page.set_input_files("input[type='file']", str(file_path))
            self.saveimg.click()