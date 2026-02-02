Feature: View and Edit Contact Details

Scenario: View and edit contact details successfully
    Given user is logged into the application
    And user navigates to the contact details page
    When user views the contact details
    And user edits the contact details
    Then contact details should be updated successfully