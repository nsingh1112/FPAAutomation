@ShellHubTest
Feature: ShellHubTest
	In order to verify searching in ShellHub works fine, this test has been written

@shellhubtest1
Scenario: Test Shell Hub page
    Given user navigates to the Shell hub site
    When user searches for keyword "Functional Excellence Testing" from search-box
    Then user validates the title of the window "Search"
    When user navigates back to "https://hub.shell.com"
    And user clicks on Yammer link
    Then user verifies if totally "2" windows are displayed
    When user navigates to the child window using title "Yammer"
    And user closes the child window
    And user logs out of the application
    Then user validates the Select account screen