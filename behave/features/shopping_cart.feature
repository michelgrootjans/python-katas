Feature: shopping cart
  As a customer
  I want to know the total of my shopping cart
  so I can decide when to stop shopping

  Scenario: an empty shopping cart
    Given an empty shopping cart
    Then the total of my shopping cart is € 0.00

  Scenario: buying one item
    Given an empty shopping cart
    And a chair is for sale for € 10.00
    When I add a chair to my shopping cart
    Then the total of my shopping cart is € 10.00

  Scenario: buying an items twice
    Given an empty shopping cart
    And a chair is for sale for € 10.00
    When I add 2 chairs to my shopping cart
    Then the total of my shopping cart is € 20.00

  Scenario: buying multiple items
    Given an empty shopping cart
    And a chair is for sale for € 10.00
    And a table is for sale for € 20.00
    When I add 4 chairs to my shopping cart
    And I add a table to my shopping cart
    Then the total of my shopping cart is € 60.00
