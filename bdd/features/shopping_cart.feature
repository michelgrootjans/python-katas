Feature: Shopping cart
  As a customer
  I want to know the total of my shopping cart before checking out
  so I can decide when to stop shopping

Scenario: Add a single item to the shopping cart
  Given an item costing € 1.00
    And an empty shopping cart
   When I add the item to my shopping cart
   Then the total of my shopping cart is € 1.00

Scenario: Add a single item to the shopping cart
  Given an item costing € 1.00
    And an empty shopping cart
   When I add the item to my shopping cart twice
   Then the total of my shopping cart is € 1.00
