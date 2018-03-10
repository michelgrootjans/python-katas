class Catalog
  def initialize
    @products = []
  end

  def add(name, price)
    @products << Product.new(name, price)
  end

  def find(name)
    @products.find{ |p| p.name == name}
  end
end

class Product
  attr_reader :name, :price
  def initialize(name, price)
    @name = name
    @price = price
  end
end