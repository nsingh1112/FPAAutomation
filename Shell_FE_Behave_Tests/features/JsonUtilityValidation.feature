@gorest
Feature: Validate Json comparison Utility
 @getrequest
  Scenario: Validating the Json Utility methods
    When user sends a GET request to retrieve user details
    Then user compare json response with expected data
    Then user search value in response with key
    Then user gets the specific node value
    Then user finds the difference between json responses
    Then user checks values presence in the response text