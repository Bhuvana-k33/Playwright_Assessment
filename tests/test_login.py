from pytest_bdd import scenarios

scenarios("../features/login.feature")

from stepDefinitions.test_login_steps import *