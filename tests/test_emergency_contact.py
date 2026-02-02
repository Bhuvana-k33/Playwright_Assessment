import json

from pages.emergency_contact import EmergencyContact


def test_adddelete_emergencycontact(logged_in_page):
    with open("test_data/test_details.json") as f:
        contacts = json.load(f)["emergency_contacts"]
    emergencycontact = EmergencyContact(logged_in_page)
    emergencycontact.open()

    for contact in contacts:
        emergencycontact.add_emergency_contact(contact)

    #emergencycontact.delete_emergency_contact()

    emergencycontact.add_attachments()
