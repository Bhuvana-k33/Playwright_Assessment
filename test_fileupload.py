import time
from sys import path

from playwright.sync_api import Page

def test_fileupload(page: Page):

    page.goto("https://the-internet.herokuapp.com/upload")
    page.get_by_role("heading", name="File Uploader").click()
    page.set_input_files("input[type='file']",r"C:\Users\Daffolap-1080\PycharmProjects\PythonProject\File_upload.txt")
    time.sleep(5)
