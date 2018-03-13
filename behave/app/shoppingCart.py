class ShoppingCart(object):
  def __init__(self):
    self.items = []

  def add(self, qty, product):
    self.items.append(ShoppingCartItem(qty, product))

  def total(self):
    return sum(item.price() for item in self.items)

class ShoppingCartItem(object):
  def __init__(self, qty, product):
    self.qty = qty
    self.product = product

  def price(self):
    return self.qty * 10