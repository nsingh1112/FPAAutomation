@web @FPA @FPADocuments

Feature: Checking the Documents functionality

  Scenario Outline: Validating Database
    Given Launch the browser and navigate to the url
    When  The user Clicks on Documents "<documentsItems>"
    Then  The user validates "<documentsItems>" page title
    And  The user validates data Fields
    And  The user enters document type and search by text and click on search button
    And  The user Validates the Label
    And The user Clicks on file name and verify the file is opened in new tab
    Then The user click on Clear button
   # When handle the SSO using actions
    #Then The user validates FileName
  Examples: Documents Items
      | documentsItems       |
      | Terminal Report |
      | Invoices        |




