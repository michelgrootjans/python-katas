from behave import *
from app.shoppingCart import *
from app.catalog import *

@given(u'an empty shopping cart')
def step_impl(context):
  context.shoppingCart = ShoppingCart()

@given(u'a chair is for sale for € 10.00')
def step_impl(context):
  if not hasattr(context, 'catalog'):
    context.catalog = Catalog()
  context.catalog.add("chair", 10.00)

@when(u'I add a chair to my shopping cart')
def step_impl(context):
  product = context.catalog.find("chair")
  context.shoppingCart.add(1, product)

@when(u'I add 2 chairs to my shopping cart')
def step_impl(context):
  product = context.catalog.find("chair")
  context.shoppingCart.add(2, product)

@then(u'the total of my shopping cart is € {price}')
def step_impl(context, price):
  assert context.shoppingCart.total() == float(price), "expected: " + price + "; actual: " + str(context.shoppingCart.total())
