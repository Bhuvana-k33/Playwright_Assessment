
import pytest
@pytest.mark.smoke
def test_login(page):
    page.goto("https://www.saucedemo.com/")
    page.fill('#user-name', 'standard_user')
    page.fill('#password', 'secret_sauce')
    page.click('#login-button')

@pytest.mark.regression
def test_all_items(page):
    page.goto("https://www.saucedemo.com/")
    page.fill('#user-name', 'standard_user')
    page.fill('#password', 'secret_sauce')
    page.click('#login-button')
    page.click('#react-burger-menu-btn')

@pytest.mark.skip(reason="Not Required Now")
def test_add_to_cart(page):
    page.goto("https://www.saucedemo.com/")
    page.fill('#user-name', 'standard_user')
    page.fill('#password', 'secret_sauce')
    page.click('#login-button')
    page.click('#add-to-cart-sauce-labs-backpack')