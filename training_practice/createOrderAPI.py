import json
import time

import pytest
from playwright.sync_api import Playwright, expect
from pathlib import Path

from utils.getToken import ApiUtils

BASE_DIR = Path(__file__).resolve().parent.parent   # adjust if needed
file_path = BASE_DIR /"PythonProject" / "test_data" / "creds.json"

with open(file_path) as f:
    data = json.load(f)
    user_credentials_list = data["user_credentials_list"]

@pytest.mark.parametrize('user_credentials',user_credentials_list)
def test_playwrightBasics(playwright : Playwright,user_credentials):
    print(type(user_credentials), user_credentials)

    userName = user_credentials["userName"]
    password = user_credentials["password"]

    # API Call to get order id
    apiUtils = ApiUtils()
    orderId = apiUtils.createOrder(playwright, userName, password)
    print(orderId)

    #Ui
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")

    #Login page
    page.locator("#userEmail").fill(userName)
    page.locator("#userPassword").fill(password)
    page.locator("#login").click()

    #dashboard
    page.get_by_role("button", name="ORDERS").click()

    #OrderDetails Page
    row = page.locator("tr").filter(has_text=orderId)
    expect(row).to_be_visible()
    time.sleep(5)