@parallel
Feature: testingparallel
  Scenario: parallel run
    When run in parallel "ShellHubTest.feature"
    And run in parallel "FileUtilityValidation.feature"
