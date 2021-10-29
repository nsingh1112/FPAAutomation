Feature: Android Demo
  Scenario: Test light theme controls in views
    Given I have launched the apidemos app
    When  I test views
    Then  I verify checkbox and radio buttons

  Scenario: Test Popups
	When I Click on Views
	Then I verify popups

  Scenario: Test Lists and ExpandableLists
	When I Click on Views
	And  I Click on Expandable Lists
	Then I Verify all lists

  Scenario: Test Drag and Drop
	When I Click on Views
	Then I verify DragAndDrop

  Scenario: Test Alerts
	When I Click on App
	Then I verify alerts

  Scenario: Test Date Widgets
	When I Click on Views
	And  I click on Date
	Then I select Date

  Scenario: Test Gallery
	When I Click on Views
	And I Click on Gallery
	Then I Select Picture