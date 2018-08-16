# Created by bob_bao at 2017/11/25
Feature: ECS instance feature
  This is used to test ecs instance related API with Python SDK

  Scenario: Create ECS instance
    When I create an ECS instance
    Then I could see the new instance