import time
from sys import path

from playwright.sync_api import Page

def test_fileupload(page: Page):

    page.goto("https://the-internet.herokuapp.com/upload")
    page.get_by_role("heading", name="File Uploader").click()
    page.set_input_files("input[type='file']", r"/File_upload.txt")
    page.click("#file-submit")

    file_name=page.locator("#uploaded-files").text_content()
    assert "File_upload.txt" in file_name
    print("File name matched")
    time.sleep(5)

def test_filedownload(page: Page):
    file_name= "../File_upload.txt"
    page.goto("https://the-internet.herokuapp.com/download")
    page.click(f"text={file_name}")