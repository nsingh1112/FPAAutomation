@gorest
Feature: Validate API with Requests
  @getrequest
  Scenario: GET Request validation using the base uri from INI file
    When user sends a GET request to retrieve user details
    Then user validates if the response status is "200"
    Then user verifies if "male" user is available in the response body

  @postrequest
  Scenario Outline: POST Request validation
    When user sends a POST request to create new "<User>"
    Then user validates if the Create User response status is 201
    Then user validates if the "<User>" has been created successfully
    Examples:
      | User  |
      | user1 |
      | user2 |

  @getrequest
  Scenario: GET Request validation using the BaseUri from json file
    When user sends a GET request to retrieve user details
    Then user validates if the response status is "200"