Feature: Shopping Cart
  As a logged-in user I want to add and remove items from the cart.

  Background:
    Given I am logged in as "standard_user"

  Scenario: Add one item to cart
    Given I am on the inventory page
    When I add the first product to the cart
    Then the cart badge should show "1" item

  Scenario: Remove one item from cart
    Given I am on the inventory page
    And I add the first product to the cart
    And the cart badge should show "1" item
    When I remove the first product from the cart
    Then the cart badge should not be visible

  Scenario: Verify cart badge count with multiple items
    Given I am on the inventory page
    When I add the first product to the cart
    And I add the second product to the cart
    Then the cart badge should show "2" items

  Scenario: Remove item from cart page
    Given I am on the inventory page
    And I add the first product to the cart
    When I open the cart
    And I remove the first item from the cart
    Then the cart should have "0" items
