@hybridApp @mobile
Feature: Hybrid App Demo
  Scenario: Test the search box
    Given I launched the mobile native chrome app
    When  I am clicking on search and pass values to search
    Then  I Search for the text

  Scenario: Click on the link
    When I test the web_view
    Then I replace the search text
