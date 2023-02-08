@web @FPA

Feature: Checking the FPA functionality
  Scenario: Validating FPA Left Menu and SubMenu
    Given Launch the browser and navigate to the url
    When  The user validates the homepage
    When  The user validates the dashboardItems


  Scenario: Validating FPA Unprocessed Record data
    # Given Launch the browser and navigate to the url
    When  The user Clicks on Unprocessed records under RECONCILIATION
    # When  The user validates the Reconciled Data page controls

  Scenario: Validating FPA Reconciled data
    # Given Launch the browser and navigate to the url
    When  The user Clicks on Reconciled Data under RECONCILIATION
    When  The user validates Reconciled Data page title
    Then  The user enters received date and click on search button
    # When  The user validates the Reconciled Data page controls




