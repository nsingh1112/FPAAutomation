@web @FPAReconcilation

Feature: Checking the FPA Reconcilation functionality

  Scenario: Validating FPA Reconciled data
    Given Launch the browser and navigate to the url
    When  The user Clicks on Reconciled Data under RECONCILIATION
    Then  The user validates Reconciled Data page title
    And  The user validates Reconciled Data Fields
    And  The user enters received date and click on search button
    And  The user Validates the Reconciled ReportPage Label
    #Then The user enters received date and click on Clear button



  Scenario: Validating Reprocessed
    When The user Clicks on Reprocessed
    Then The user validates Reprocessed page title
    And  The user validates Reprocessed Data Fields
    And  The user enters received date and click on search button
    And  The user Validates the Reprocessed ReportPage Label
    Then The user enters received date and click on Clear button



