from behave import *
from app.shoppingCart import *
from app.catalog import *

@given(u'an empty shopping cart')
def step_impl(context):
  context.shoppingCart = ShoppingCart()

@given(u'a {product} is for sale for € {price}')
def step_impl(context, product, price):
  if not hasattr(context, 'catalog'):
    context.catalog = Catalog()
  context.catalog.add(product, float(price))

@when(u'I add a {name} to my shopping cart')
def step_impl(context, name):
  product = context.catalog.find(name)
  context.shoppingCart.add(1, product)

@when(u'I add {qty:d} {name}s to my shopping cart')
def step_impl(context, qty, name):
  product = context.catalog.find(name)
  context.shoppingCart.add(qty, product)

@then(u'the total of my shopping cart is € {price}')
def step_impl(context, price):
  assert context.shoppingCart.total() == float(price), "expected: " + price + "; actual: " + str(context.shoppingCart.total())
