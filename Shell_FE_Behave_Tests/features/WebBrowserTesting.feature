@mobileWeb @mobile @chrome
Feature:Web Browser Demo
  Scenario: Test the web browser
    Given I have launched the chrome app
    When  I am passing the URL
    Then  I verify it landed on the corresponding URL
    Then  I am passing the username
    Then  I verify it is landed on the Authentication system page