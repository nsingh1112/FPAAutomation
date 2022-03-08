@gorest
Feature: Validate API with Requests
  @getrequest
  Scenario: GET Request validation
    When user sends a GET request to retrieve user details
    Then user validates if the response status is "200"
    Then user verifies if "male" user is available in the response body

  @postrequest
  Scenario: POST Request validation
    When user sends a POST request to create new user
    Then user validates if the Create User response status is 201
    Then user validates if the user has been created successfully

