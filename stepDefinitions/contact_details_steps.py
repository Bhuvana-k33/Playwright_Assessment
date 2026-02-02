import pytest
from pytest_bdd import given, when, then
from pages.contact_details import ContactDetails
from playwright.sync_api import expect


@given("user is logged into the application")
def user_logged_in(logged_in_page):
    # logged_in_page fixture already handles login
    return logged_in_page

@pytest.fixture

@given("user navigates to the contact details page")
def contact_details_page(logged_in_page):
    contact_details = ContactDetails(logged_in_page)
    contact_details.open()
    return contact_details


@when("user views the contact details")
def view_contact_details(contact_details_page):
    contact_details_page.view_contactdetails()


@when("user edits the contact details")
def edit_contact_details(contact_details_page):
    contact_details_page.edit_contactdetails()


@then("contact details should be updated successfully")
def verify_contact_details_updated(contact_details_page):
    # Example validation – adjust locator/message as per your app
    contact_details_page.verify_success_message()