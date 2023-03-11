@web @FPA @FPADashboard

Feature: Checking the Dashboard Functionality

  Scenario: Validating FPA Left Menu and SubMenu
    Given Launch the browser and navigate to the url
    When  The user validates the homepage
    When  The user validates the dashboardItems

  Scenario: Validating Unprocessed
    When The user Clicks on Unprocessed
    Then The user validates the Unprocessed Page title
    And The user validates total no of records
    Then The user validates Unprocessed Data Fields

  Scenario Outline: Validating Reconciled data, Reprocessed
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


  Scenario: Validating Entered In DEX
    When  The user Clicks on Entered In DEX Dashboard Items
    Then  The user validates the Entered In DEX Page title
    And  The user validates Entered In DEX Data Fields
    And  The user enters received date in Entered In DEX and click on search button
    And  The user Validates the Label displayed in the Entered In DEX
    Then The user enters received date and click on Clear button


  Scenario: Validating Failed To Enter In DEX
    When  The user Clicks on Failed To Enter In DEX Dashboard Items
    Then  The user validates the Failed To Enter In DEX Page title
    And  The user validates Failed To Enter In DEX Data Fields
    And  The user enters contract ID and click on search button
    And  The user Validates the Label displayed in the Failed To Enter In DEX
    Then The user enters received date and click on Clear button




