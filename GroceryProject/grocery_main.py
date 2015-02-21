# Here is our initial list of items for our store. This will eventually live in another file once we
# have set up a few more of the basic items.
items = {apples: {price: 1, qyt: 5}, kashi: {price: 2, qty:15}, mops: {price: 5, qty: 20}}

# This will create a basic profile for users. Later in the program buyers/sellers will be distinguished
class Profile(object):
  def __init__(self, first_name, last_name, money, password)
    self.first_name = first_name
    self.last_name = last_name
    self.money = money
    self.password = password


class Buyer(Profile):
  def Cart(self):
    self.inventory = { }
    