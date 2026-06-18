@TC_007 @account_overview
Feature: TC_007 - Automation Prints Displayed Amount
  As a test engineer
  I want the automation to capture and print the account balance
  So that the amount is visible in the execution logs

  Scenario: Verify automation prints displayed amount in logs
    Given the user is logged in with their registered account
    When the user navigates to the account overview page
    And the automation captures the displayed account balance
    Then the balance amount should be printed to the execution logs
    And the printed balance should not be empty
