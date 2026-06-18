@TC_002 @registration
Feature: TC_002 - Registration with Valid Details
  As a new user
  I want to create an account with valid details
  So that I can access ParaBank online banking services

  Scenario: Verify user can create a new account with valid details
    Given the user is on the ParaBank homepage
    When the user clicks the Register link
    And the user fills all required fields with valid details
    And the user submits the registration form
    Then the account should be created successfully
    And a welcome message should be displayed
