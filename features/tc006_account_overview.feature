@TC_006 @account_overview
Feature: TC_006 - Account Amount Displayed After Login
  As a logged-in ParaBank user
  I want to see my account balance on the overview page
  So that I can confirm the balance is visible and accessible

  Scenario: Verify account amount is displayed after login
    Given the user is logged in with their registered account
    When the user navigates to the account overview page
    Then the account overview page title should be visible
    And at least one account with a balance should be displayed
