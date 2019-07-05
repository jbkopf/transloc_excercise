Feature: test transloc

  Scenario: Can log in with valid user and password
    Given I go to transloc
    When I enter a valid user and password
    And I click login
    Then I see I am logged in

  Scenario: Cannot login with invalid credentails
    Given I go to transloc
    When I enter an invalid user and password
    And I click login
    Then I see invalid credentials error
    And I see I am not logged in