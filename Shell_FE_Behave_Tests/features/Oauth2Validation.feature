@gorest
Feature: Validate OATH2 API with Requests
 @oathrequest
  Scenario: OATH2 Request validation
    When user sends a POST request to retrieve access token
    Then user validates if the response status is "200"
    Then user sends a GET request to access details