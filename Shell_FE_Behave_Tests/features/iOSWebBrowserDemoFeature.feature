@mobileWeb @mobile @safari
Feature:Web Browser Demo
  Scenario: Test the web browser
    Given I have launched the safari app
    When  I am testing the background and foreground methods
    When  I am passing the URL
    Then  I verify it landed on the corresponding URL
    Then  I am passing the username
    Then  I verify it is landed on the Authentication system page