Feature: shopping cart total
  As a customer
  I want to know the total of my shopping cart
  so that I can decide when to go to the checkout

  Scenario: an empty shopping cart
    Given an empty shopping cart
    Then the total of my shopping cart is € 0.00

  Scenario: a shopping cart with one item
    Given an empty shopping cart
    And a chair is for sale at € 10.00
    When I add a chair to my shopping cart
    Then the total of my shopping cart is € 10.00

  Scenario: a shopping cart with the same item twice
    Given an empty shopping cart
    And a chair is for sale at € 10.00
    When I add 2 chairs to my shopping cart
    Then the total of my shopping cart is € 20.00

  Scenario: a shopping cart with multiple items
    Given an empty shopping cart
    And a chair is for sale at € 10.00
    And a table is for sale at € 20.00
    When I add 4 chairs to my shopping cart
    And I add a table to my shopping cart
    Then the total of my shopping cart is € 60.00