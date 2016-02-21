# Defining classes
import random

class Bicycle:
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
    
    def __str__(self):
        print (None)
    
class Shop:
    def __init__(self, name, markup):
        self.name = name
        self.markup = markup
        self.inventory = []
        self.profit = 0
        self.current_customers = []
    
    # Adding customers to current_customers list    
    def customer_add(self, *customers):
        for customer in customers:
            self.current_customers.append(customer)
            
    def customer_list(self):
        print ("Current Shop: {}".format(self.name))
        for customer in self.current_customers:
            print ("")
            print ("Name: {}".format(customer.name))
            print ("Funds: {}".format(customer.fund))

    # Pulling in the shop name and displaying the bicycles that are available plus the markup
    def inventory_count(self):
        print ("Current Shop: {}".format(self.name))
        for bicycle in self.inventory:
            print ("Model: {}".format(bicycle.model))
            print ("Price: {}".format(bicycle.cost*(1 + self.markup)))
            print ("Weight: {}".format(bicycle.weight))
            print ("")
            
    def purchase_bicycle(self, *bicycles):
        for bicycle in bicycles:
            self.inventory.append(bicycle)
            
    def sell_bicycle(self, bicycle, customer):
        self.inventory.remove(bicycle)
        customer.owned_bicycles.append(bicycle)
        customer.fund -= (bicycle.cost * (1 + self.markup))
        print ("")
        print ("{} just bought {} and has {} remaining".format(customer.name, bicycle.model, customer.fund))

class Customer:
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        self.owned_bicycles = []
    
    #Specifying the models that customer is able to afford    
    def potential_models(self, shop):
        print ("Showing models that {} can afford".format(self.name))
        for bicycle in shop.inventory:
            if bicycle.cost * (1 + shop.markup) < self.fund:
                print (bicycle.model)

# Specifying bicycles
bicycle_1 = Bicycle("Bike 1", 100, 100)
bicycle_2 = Bicycle("Bike 2", 90, 200)
bicycle_3 = Bicycle("Bike 3", 80, 300)
bicycle_4 = Bicycle("Bike 4", 70, 400)
bicycle_5 = Bicycle("Bike 5", 60, 500)
bicycle_6 = Bicycle("Bike 6", 50, 600)

# Adding shops
shop_1 = Shop("Shop 1", .20)

# Specifying customers
customer_1 = Customer("Customer 1", 200)
customer_2 = Customer("Customer 2", 500)
customer_3 = Customer("Customer 3", 1000)

# Purchase inventory by adding bicycles to shop inventory
shop_1.purchase_bicycle(bicycle_1, bicycle_2, bicycle_3, bicycle_4, bicycle_5, bicycle_6)

# Adding customers to shop_1
shop_1.customer_add(customer_1, customer_2, customer_3)

# Print current inventory
shop_1.inventory_count()

# Print bikes that customers can afford
for customer in shop_1.current_customers:
    customer.potential_models(shop_1)
    
# Have customer buy a bike
shop_1.sell_bicycle(bicycle_1, customer_1)
shop_1.sell_bicycle(bicycle_2, customer_2)
shop_1.sell_bicycle(bicycle_3, customer_3)