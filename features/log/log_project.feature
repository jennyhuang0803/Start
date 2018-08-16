# Created by bob_bao at 2017/12/19
Feature: LOG Project API
  This is used to test log project API
  Should include create

  Scenario: Create Log Project
    When I create a log project
    Then I could see the new created log project

  Scenario: Delete Log Project
    Given I have a log project
    When I delete the log project
    Then I could not see the log project