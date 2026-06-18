@TC_004 @registration @negative
Feature: TC_004 - Duplicate Username Validation
  As a user trying to register
  I want to see an error when I use an already registered username
  So that I know to choose a different username

  Scenario: Verify duplicate username validation
    Given the user is on the ParaBank homepage
    When the user clicks the Register link
    And the user registers successfully with a unique username
    And the user clicks the Register link again
    And the user attempts to register with the same username
    Then the system should display a username already exists error
