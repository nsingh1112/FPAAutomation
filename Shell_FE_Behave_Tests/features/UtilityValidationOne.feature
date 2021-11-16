@Utilities
Feature: Utilities validation tutorials point - Feature One

  Scenario: Validate the working of methods related to text boxes
    Given user navigates to the TutorialsPoint site
    When user enters "Henry" in First name
    And user enters "Adams" in Last name
    Then user validates the "First name" label in First name textbox
    When user copies the value from Firstname textbox
    And user pastes the value into Lastname textbox
    Then user validates if the value "Henry" is present in Lastname textbox using JSExecutor
    When user clears the Firstname textbox using actions
    And user enters "Adams" in Last name
    And user copies the value from Lastname textbox into Firstname textbox
    Then user validates the value "Adams" in Last name textbox
    When user clears the Firstname textbox using actions
    And user clears the Last name textbox
    When user enters "Thomas" in first name using JSExecutor
    And user enters "Shelby" in Last name using actions
    When user prints the color of the Firstname label
    Then user validates the "Years of Experience" label using JSExecutor

  Scenario: Validate the working of methods related to Radio buttons, checkboxes and dropdowns
    Given user navigates to the TutorialsPoint site
    When user selects the Male radiobutton
    Then user validates if the Male radiobutton is selected
    Then user validates if Female radiobutton is enabled
    Then user validates if Female radiobutton is not selected
    When user selects the Manual Tester checkbox using checkbox method
    And user selects the Automation Tester checkbox using click method
    And user unselects the Automation Tester checkbox
    Then user asserts if the Automation Tester checkbox has been unselected
    When user selects YoE as 7 using JSExecutor click
    And user changes the YoE selection as 5 using actions click
    When user selects continent as "Europe" using visible text
    Then user validates the selected value "Europe" from dropdown
    When user retrieves the attributes of Male radiobutton
    When user retrieves the attributes of Female radiobutton via JSExecutor
    Then user updates the "value" attribute to "Transgender" and validates the change