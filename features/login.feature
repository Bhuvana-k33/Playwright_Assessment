Feature: Login functionality

  Scenario Outline: Successful login with Valid Credentials
    Given user is on the login page
    When user enters username "<username>" and password "<password>"
    Then user should be logged in successfully
    Examples:

    | username                             |   password      |
    | Admin                                |   admin123      |

  Scenario Outline: Unsuccessful login with invalid credentials

    Given user is on the login page
    When user enters username "<username>" and password "<password>"

    Then login should fail with an error message
    Examples:
      | username | password  |
      | Admin    | wrong123  |
      | Wrong    | admin123  |
      | Wrong    | wrong123  |