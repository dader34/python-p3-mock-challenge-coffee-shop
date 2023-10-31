class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not hasattr(self,"name") and isinstance(name,str) and len(name):
            self._name = name
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in Order.all if order.coffee == self})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        all_orders = self.orders()
        return sum([order.price for order in Order.all if order.coffee == self]) / len(all_orders)

class Customer:

    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if isinstance(name,str) and len(name)>0 and len(name) <16 :
            self._name = name
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in Order.all if order.customer == self})
    
    def create_order(self, coffee, price):
        new_order = Order(self,coffee,price)
        return new_order
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,price):
        if not hasattr(self,"price") and isinstance(price,float):
            self._price = price
    
