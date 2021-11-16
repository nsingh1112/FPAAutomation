Feature: Utilities validation tutorials point - Feature One
#  Scenario: Validate the working of Browser Utilities
    Given user navigates to Academy site
    When user navigates back
    Then user validates the title equality using Wait utilities
    Then user validates if the title contains the expected value using Wait Utilities
#    Then user validates the url equality using Wait Utilities
    Then user validates if the url contains the expected value using Wait Utilities
    When user navigates forward
    When user refreshes the page
    Then user waits for the text "Practice Page" to be present in the page
    When user refreshes the page
    Then user waits for the value "option1" to be present in the page

  Scenario: Validate child window, alert and frame handling
    Given user navigates to Academy site
#    When user clicks on the Hide button
#    Then user verifies if the text box is hidden
#    When user clicks on the Show button
#    Then user verifies if the text box is shown
    When user clicks on Open window button
    Then user verifies the number of windows "2"
    When user switches to child window
    And user switches to parent window
    And user switches to child window and closes it
    And user clicks on Open window button
    Then user switches to child window by title, asserts and closes it
    When user clicks on Open Tab button
    Then user verifies the number of windows "2"
    When user switches to child window
    And user switches to parent window
    And user switches to child window and closes it
    And user clicks on Open Tab button
    Then user switches to child tab by title, asserts and closes it
    When user clicks on Alert button
    Then user validates the Alert text
    Then user accepts Alert
    When user clicks on Confirm button
    Then user validates the Alert text
    Then user accepts confirm alert
    When user clicks on Confirm button
    Then user dismisses confirm alert
##    When user switches to the frame
##    When user selects blog in frame
##    When scrolls down in frame
    When user selects value from dropdown
    When user scrolls down window
    And user scrolls the window up
    When user hovers mouse
    Then validates if options are displayed

