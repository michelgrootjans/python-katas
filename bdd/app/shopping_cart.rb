class ShoppingCart
  def initialize
    @content = []
  end
  
  def add(qty, product)
    @content << ShoppingCartItem.new(qty, product)
  end

  def total
    @content.sum(&:price)
  end
end

class ShoppingCartItem
  def initialize(qty, product)
    @qty = qty
    @product = product
  end

  def price
    @qty * @product.price
  end
end