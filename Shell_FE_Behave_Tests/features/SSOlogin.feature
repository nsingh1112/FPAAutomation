@web @SSOalert

Feature: Checking the login functionality
  Scenario: Handling SSO in Shell hub page
    Given Launch th chrome browser and navigate to Shell hub home page
    When Pass username to the username field
    When handle the SSO using actions
    Then It should land on stay sign in page


