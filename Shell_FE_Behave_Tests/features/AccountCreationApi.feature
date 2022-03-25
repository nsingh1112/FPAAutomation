@accountcreation
Feature: Validate Account Creation
 @oathrequest
  Scenario: Account Request validation
   Given user logs into Salesforce application as "System Administrator" role
   When user creates the account
   And user fetches the account ID
