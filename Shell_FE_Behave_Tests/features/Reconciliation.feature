@web @FPA @FPAReconciliation

Feature: Checking the Reconciliation functionality

  Scenario Outline: Validating Reconciliation
    Given Launch the browser and navigate to the url
    When  The user Clicks on Reconciliation "<reconciliationItems>"
    Then  The user validates Reconciliation "<reconciliationItems>" page title
    And  The user validates Reconciliation "<reconciliationItems>" data Fields
    And  The user Validates Reconciliation Label
  Examples: Reconciliation Items
      | reconciliationItems |
      | Unprocessed Records |
      | Reconciled Data     |


  Scenario Outline: Updating Unprocessed Record and Reconciled Data Quantity and Terminal ref Id
    When  The user Clicks on Reconciliation "<reconciliationItems>"
    Then The user selects and updates a Reconciliation "<reconciliationItems>"
    And The user validates Reconciliation "<reconciliationItems>" record
  Examples: Reconciliation Items
      | reconciliationItems |
      | Unprocessed Records |
      | Reconciled Data     |




