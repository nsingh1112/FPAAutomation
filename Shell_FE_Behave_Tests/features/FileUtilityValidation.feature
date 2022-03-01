@FileUtility
Feature: File Utility methods validation
  Scenario: Validation of all methods available in File Utilities
    When user reads the values available in excel by cell value
    When user reads the values available in excel by rowname
    When user reads the values from json file
    When user reads the values from json string
    When user converts dictionary into json string
    When user writes into json file
    When user writes into existing excel sheet
    When user writes into new excel sheet
    When user writes into excel by cellname
    When user reads the values available in csv by rowname
    When user reads the root element's values from xml
    When user reads the child element's values from xml

@ExcelComparison
  Scenario: Validate Excel comparison
    When user compares the Excel files "File1.xlsx" and "File2.xlsx" for equality
