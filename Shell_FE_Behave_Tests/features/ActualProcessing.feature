@web @FPA @FPAActualProcessing

Feature: Checking the ActualProcessing functionality

  Scenario Outline: Validating ActualProcessing
    Given Launch the browser and navigate to the url
    When  The user Clicks on Actual Processing "<actualProcessingItems>"
    Then  The user validates Actual Processing "<actualProcessingItems>" page title
    And  The user validates Actual Processing "<actualProcessingItems>" data Fields
    And  The user Validates Actual Processing Label
  Examples: ActualProcessing Items
      | actualProcessingItems |
      | Create |
      | Manage Actuals |
      | Actual Volumes |




