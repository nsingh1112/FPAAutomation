@web @FPA @FPADatabase

Feature: Checking the Database functionality

  #Scenario Outline: Validating Documents DB
   # Given Launch the browser and navigate to the url
   # When  The user Clicks on documentItems "<documentsItems>" and validates record from database
    #Examples: Documents Items
     # | documentsItems  |
     # | Terminal Report |
     # | Invoices        |


  #Scenario Outline: Validating Logs DB
  #  When  The user Clicks on LogsItems "<logsItems>" and validates record from database
    #Examples: Logs Items
     # | logsItems  |
     # | Reconciliation Errors |
      #| Actual's Errors       |


  Scenario: Validating Logs DB
    When  The user varifies the aggregated data columns in database



