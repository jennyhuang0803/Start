# Created by bob_bao at 2017/12/1
Feature: VPC instance API
  This is used to test VPC instance API.
  Should include create, delete, describe, modify related functions

  @vpc_instance_release
  Scenario: Create VPC instance
    When I create a VPC instance
    Then I can see the new created instance

  @vpc_instance_release
  Scenario: Modify VPC instance attributes
    Given I have a VPC instance
    When I update the attributes of the VPC instance
    Then I can see the updated attributes

  Scenario: Delete VPC instance
    Given I have a VPC instance
    When I delete the VPC instance
    Then I can not see the instance