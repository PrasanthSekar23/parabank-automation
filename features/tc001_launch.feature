@TC_001 @launch
Feature: TC_001 - Launch Application
  As a user
  I want to verify that the ParaBank website opens successfully
  So that I can confirm the application is accessible

  Scenario: Verify ParaBank website opens successfully
    Given the browser is available
    When I navigate to the ParaBank URL
    Then the ParaBank homepage should load successfully
    And the page title should contain "ParaBank"
    And the login panel should be visible
