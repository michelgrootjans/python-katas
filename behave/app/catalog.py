class Catalog(object):
  def __init__(self):
    self.products = []

  def add(self, name, price):
    self.products.append(Product(name, price))

  def find(self, name):
    return Product("chair", 10.00)

class Product(object):
  def __init__(self, name, price):
    pass