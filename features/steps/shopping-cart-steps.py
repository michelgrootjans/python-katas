from nose.tools import *
from app.shopping_cart import *

@given(u'an empty shopping cart')
def step_impl(context):
    context.shopping_cart = 0

@given(u'a {product_name} is for sale at € {price:f}')
def step_impl(context, product_name, price):
    pass

@when(u'I add a {product_name} to my shopping cart')
def step_impl(context, product_name):
    pass

@when(u'I add {qty:d} {product_name}s to my shopping cart')
def step_impl(context, qty, product_name):
    pass

@then(u'the total of my shopping cart is € {total:f}')
def step_impl(context, total):
    assert_equals(context.shopping_cart, total)
