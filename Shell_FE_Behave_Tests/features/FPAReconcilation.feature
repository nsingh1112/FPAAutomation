@web @FPAReconcilation

Feature: Checking the FPA Reconcilation functionality

  Scenario Outline: Validating FPA Reconciled data, Reprocessed
    Given Launch the browser and navigate to the url
    When  The user Clicks on Reconciled Data under RECONCILIATION
    Then  The user validates Reconciled Data page title
    And  The user validates Reconciled Data Fields
    And  The user enters received date for "<dashboardItems>" and click on search button
    And  The user Validates the Reconciled ReportPage Label
    Then The user enters received date and click on Clear button

    Examples: Dashboard Items
      | dashboardItems |
      | Reconciliation |
      | Reprocessed    |




