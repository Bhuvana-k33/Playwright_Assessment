from playwright.sync_api import expect
import re
from pathlib import Path
from pages.base_page import BasePage

class PersonalDetails(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.my_info_menu = page.get_by_role("link", name="My Info")
        self.personal_details_tab = page.get_by_role("link", name="Personal Details")
        self.fname= page.get_by_placeholder("First Name")
        self.mname = page.get_by_placeholder("Middle Name")
        self.lname = page.get_by_placeholder("Last Name")
        self.savebtn=page.get_by_role("button",name="save").nth(0)
        self.profilepicture=page.locator("img.employee-image")
        self.imageupload=page.locator("button.employee-image-action")
        self.imagesavebtn=page.get_by_role("button",name="Save")
        self.failure_msg=page.get_by_text("Attachment Size Exceeded")
        #self.success_msg = page.locator(".toast-success")


    def open(self):
        self.my_info_menu.click()
        self.personal_details_tab.click()

    def view_personaldetails(self):
        expect(self.page).to_have_url(re.compile("viewPersonalDetails"))

    def edit_personaldetails(self):
        self.fname.click()
        self.fname.fill("Andrew")
        self.mname.fill("Roxy")
        self.lname.fill("Thomas")
        self.savebtn.click()

    def profileimgupload(self,file_path:Path):
        self.profilepicture.click()
        self.imageupload.click()
      #  file_path = Path(__file__).parent.parent /"sizeless_1MB.jpeg"
        self.page.set_input_files("input[type='file']", str(file_path))
        self.imageupload.click()

    def verify_success(self):
        expect(self.failure_msg).to_have_count(0)

    def verify_failure(self):
        expect(self.failure_msg).to_be_visible()