Feature: test transloc

  Scenario: Can log in with valid user and password
    Given I go to transloc
    When I enter a valid user and password
    And I click login
    Then I see I am logged in