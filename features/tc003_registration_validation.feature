@TC_003 @registration @negative
Feature: TC_003 - Mandatory Field Validation
  As a user on the registration page
  I want to see validation errors when required fields are left empty
  So that I understand which fields are mandatory

  Scenario: Verify mandatory field validation on empty form submission
    Given the user is on the ParaBank homepage
    When the user clicks the Register link
    And the user submits the registration form without filling any fields
    Then validation error messages should be displayed for required fields
    And the error for first name should be shown
    And the error for last name should be shown
    And the error for address should be shown
    And the error for city should be shown
    And the error for state should be shown
    And the error for zip code should be shown
    And the error for SSN should be shown
    And the error for username should be shown
    And the error for password should be shown
