Given("an empty shopping cart") do
  the[:shopping_cart] = ShoppingCart.new
end

Given("a {word} is for sale at € {float}") do |word, float|  
  the[:catalog] ||= Catalog.new
  the[:catalog].add(word, float)
end

When("I add a {word} to my shopping cart") do |word|
  product = the[:catalog].find(word)
  the[:shopping_cart].add(1, product)
end

When("I add {int} {word}s to my shopping cart") do |int, word|
  product = the[:catalog].find(word)
  the[:shopping_cart].add(int, product)
end

Then("the total of my shopping cart is € {float}") do |float|
  expect(the[:shopping_cart].total).to eq float
end