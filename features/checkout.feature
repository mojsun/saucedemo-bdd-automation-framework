Feature: Checkout
  As a logged-in user I want to complete checkout and see order confirmation.

  Background:
    Given I am logged in as "standard_user"

  Scenario: Complete checkout with valid user information
    Given I am on the inventory page
    And I add the first product to the cart
    And I open the cart
    When I proceed to checkout
    And I fill checkout information with first name "Jane" last name "Doe" postal code "12345"
    And I finish the checkout
    Then I should see the order confirmation message "Thank you for your order!"

  Scenario: Verify order confirmation details
    Given I am on the inventory page
    And I add the first product to the cart
    And I open the cart
    When I proceed to checkout
    And I fill checkout information with first name "Jane" last name "Doe" postal code "12345"
    And I finish the checkout
    Then the confirmation header should contain "Thank you for your order!"
