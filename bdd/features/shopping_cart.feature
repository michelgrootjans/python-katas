Feature: Shopping cart
  As a customer
  I want to know the total of my shopping cart before checking out
  so I can decide when to stop shopping

  Background:
    Given an empty shopping cart

Scenario: Add a single item to the shopping cart
  Given a chair is for sale at € 10.00
  When I add a chair to my shopping cart
  Then the total of my shopping cart is € 10.00

Scenario: Add an item twice to the shopping cart
  Given a chair is for sale at € 10.00
  When I add 2 chairs to my shopping cart
  Then the total of my shopping cart is € 20.00

Scenario: Add an item twice to the shopping cart
  Given a chair is for sale at € 10.00
  And a table is for sale at € 20.00
  When I add 4 chairs to my shopping cart
  And I add a table to my shopping cart
  Then the total of my shopping cart is € 60.00
