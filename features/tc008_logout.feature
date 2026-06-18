@TC_008 @logout
Feature: TC_008 - Logout
  As a logged-in ParaBank user
  I want to logout from my account
  So that my session is terminated securely

  Scenario: Verify user can logout successfully
    Given the user is logged in with their registered account
    When the user clicks the Log Out button
    Then the user should be redirected to the homepage
    And the login panel should be visible again
