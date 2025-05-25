Feature: Sending an email with attachment

  Scenario: User sends an email with an attachment
    Given the user is logged into the email inbox
    When the user composes a new message
    And adds a contact to the message
    And attaches a file to the email
    And fills in the subject "SergejTest" and body "test Sergej"
    Then the email was sent and logout
