from pytest_bdd import scenarios

scenarios("../features/contact_details.feature")

from stepDefinitions.contact_details_steps import *