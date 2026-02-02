import json

from pages.immigration import Immigration


def test_immigration (logged_in_page):
    with open("test_data/test_details.json") as f:
        contacts = json.load(f)["immigration"]
    immigration = Immigration(logged_in_page)
    immigration.open()

    for contact in contacts:
        immigration.add_immigration(contact)

    #emergencycontact.delete_emergency_contact()

    immigration.add_attachments()