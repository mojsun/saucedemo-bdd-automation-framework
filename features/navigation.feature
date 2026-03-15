Feature: Navigation and Logout
  As a logged-in user I want to log out from the side menu.

  Background:
    Given I am logged in as "standard_user"

  Scenario: Logout successfully from the side menu
    Given I am on the inventory page
    When I open the side menu
    And I click logout
    Then I should be on the login page
