from nose.tools import *
from app.shopping_cart import *

@given(u'an empty shopping cart')
def step_impl(context):
    context.shopping_cart = ShoppingCart()

@given(u'a {product_name} is for sale at € {price:f}')
def step_impl(context, product_name, price):
    if not hasattr(context, 'catalog'):
        context.catalog = Catalog()
    context.catalog.add(product_name, price)

@when(u'I add a {product_name} to my shopping cart')
def step_impl(context, product_name):
    product = context.catalog.find(product_name)
    context.shopping_cart.add(1, product)

@when(u'I add {qty:d} {product_name}s to my shopping cart')
def step_impl(context, qty, product_name):
    product = context.catalog.find(product_name)
    context.shopping_cart.add(qty, product)

@then(u'the total of my shopping cart is € {total:f}')
def step_impl(context, total):
    assert_equals(context.shopping_cart.total(), total)
