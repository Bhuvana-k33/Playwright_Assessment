from pathlib import Path

import pytest
from playwright.sync_api import Page, expect
from utils import config
from pages.login_page import LoginPage
from pages.personal_details import PersonalDetails
from utils.file_utils import get_file_size_mb
MAX_SIZE_MB = 1
base_dir=Path(__file__).resolve().parents[1]


def test_viewedit_profile(logged_in_page):
    personal = PersonalDetails(logged_in_page)
    personal.open()
    personal.view_personaldetails()
    personal.edit_personaldetails()

@pytest.mark.parametrize(
        "file_path",
        [
            base_dir / "test_data" / "sizeequal_1MB.jpg",
            base_dir / "test_data" / "sizegreater_1MB.jpg",
            base_dir / "test_data" / "sizeless_1MB.jpeg"
        ]
     )

def test_file_upload(logged_in_page,file_path):
      personal = PersonalDetails(logged_in_page)
      personal.open()
      personal.view_personaldetails()
      file_size = get_file_size_mb(file_path)
      personal.profileimgupload(file_path)

      if file_size <= MAX_SIZE_MB:
        personal.verify_success()
      else:
        personal.verify_failure()