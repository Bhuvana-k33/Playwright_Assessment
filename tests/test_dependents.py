import json

from pages.dependents import Dependents


def test_add_dependents (logged_in_page):
    with open("test_data/test_details.json") as f:
        contacts = json.load(f)["dependents"]
    dependents = Dependents(logged_in_page)
    dependents.open()

    for contact in contacts:
        dependents.add_dependents(contact)

   # dependents.delete_dependents()

    dependents.add_attachments()
