require_relative '../../app/catalog'
require_relative '../../app/shopping_cart'

Given("an item costing € {float}") do |float|
  the[:catalog] = Catalog.new
  the[:catalog].add("item", float)
end

Given("an empty shopping cart") do
  the[:shopping_cart] = ShoppingCart.new
end

When("I add the item to my shopping cart") do
  product = the[:catalog].find("item")
  the[:shopping_cart].add(1, product)
end

When("I add the item to my shopping cart twice") do
  product = the[:catalog].find("item")
  the[:shopping_cart].add(2, product)
end

Then("the total of my shopping cart is € {float}") do |float|
  expect(the[:shopping_cart].total).to eq float
end