Feature: Login
  As a user I want to log in to SauceDemo so that I can shop for products.

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I log in with username "standard_user" and password "secret_sauce"
    Then I should be on the inventory page
    And the inventory page should display products

  Scenario: Unsuccessful login with locked out user
    Given I am on the login page
    When I log in with username "locked_out_user" and password "secret_sauce"
    Then an error message should be displayed
    And the error message should contain "locked out"

  Scenario Outline: Login with different valid users
    Given I am on the login page
    When I log in with username "<username>" and password "<password>"
    Then I should be on the inventory page
    Examples:
      | username       | password     |
      | standard_user  | secret_sauce |
