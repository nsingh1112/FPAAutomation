@web @FPA @FPAReconciliation

Feature: Checking the Reconciliation functionality

  Scenario Outline: Validating Reconciliation
    Given Launch the browser and navigate to the url
    When  The user Clicks on Reconciliation "<reconciliationItems>"
    Then  The user validates Reconciliation "<reconciliationItems>" page title
    And  The user validates Reconciliation data Fields
    And  The user Validates Reconciliation Label
  Examples: Reconciliation Items
      | reconciliationItems |
      | Unprocessed Records |
      | Reconciled Data     |




