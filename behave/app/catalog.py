class Catalog(object):
  def __init__(self):
    self.products = []

  def add(self, name, price):
    self.products.append(Product(name, price))

  def find(self, name):
    for product in self.products:
      if product.name == name:
        return product
    return Product("unknown product", 0)

class Product(object):
  def __init__(self, name, price):
    self.name = name
    self.price = price