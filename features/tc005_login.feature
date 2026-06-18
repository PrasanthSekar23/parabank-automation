@TC_005 @login
Feature: TC_005 - Login with Newly Created Account
  As a registered ParaBank user
  I want to login with my newly created credentials
  So that I can access my banking account

  Scenario: Verify login with newly created account
    Given the user has a registered account from TC_002
    When the user navigates to the ParaBank homepage
    And the user enters their registered username and password
    And the user clicks the Login button
    Then the user should be logged in successfully
    And the account overview page should be displayed
