class Product(object):
    def __init__(self, name, price):
        self.price = price
        self.name = name


class Catalog(object):
    def __init__(self):
        self.products = []

    def add(self, name, price):
        self.products.append(Product(name, price))

    def find(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return Product("unknow", 0)

class ShoppingCart(object):
    def __init__(self):
        self.price = 0

    def add(self, qty, product):
        self.price += qty * product.price

    def total(self):
        return self.price