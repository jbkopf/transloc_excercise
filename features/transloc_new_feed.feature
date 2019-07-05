Feature: Test new GTFS feed

  Scenario: new feed requires publisher
    Given I log in
    And I click the New Feed button
    When I fill in all required fields
    And I click the feed-info-tab
    And I clear the publisher_name field
    And I click save
    Then I see an error that a required field is missing