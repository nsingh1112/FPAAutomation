@web @FPA @FPAReconcilation

Feature: Checking the FPA Reconcilation functionality

  Scenario Outline: Validating FPA Reconciled data, Reprocessed
    Given Launch the browser and navigate to the url
    When  The user Clicks on "<dashboardItems>"
    Then  The user validates Reconciled Data page title
    And  The user validates Reconciled Data Fields
    And  The user enters received date for "<dashboardItems>" and click on search button
    And  The user Validates the Reconciled ReportPage Label
    Then The user enters received date and click on Clear button

    Examples: Dashboard Items
      | dashboardItems |
      | Reconciliation |
      | Reprocessed    |

  Scenario: Validating Failed Reconciliation
    When  The user Clicks on Failed Reconciliation Dashboard Items
    Then  The user validates Failed Reconciliation Page title
    And  The user validates Failed Reconciliation Data Fields
    And  The user enters received date for and click on search button
    And  The user Validates the Failed Reconciliation Label
    Then The user enters received date and click on Clear button




