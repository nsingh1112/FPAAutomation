@web @FPA @FPALogs

Feature: Checking the Logs functionality

  Scenario Outline: Validating Logs Functionality
    Given Launch the browser and navigate to the url
    When  The user Clicks on Logs "<logsItems>"
    Then  The user validates Logs "<logsItems>" page title
    And  The user validates Logs "<logsItems>" data Fields
    And  The user Validates Logs Label
  Examples: Logs Items
      | logsItems |
      | Reconciliation |
      | Reconciliation Errors |
      | Actual's Errors |





