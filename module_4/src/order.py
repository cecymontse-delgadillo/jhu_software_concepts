"""
order.py - Order Class
-------------------------------------------------
This module defines the Order class, which manages a customer's pizza order.
An Order can contain multiple Pizza instances, tracks the total cost,
and keeps track of whether payment has been made.

Classes:
    Order: Represents a customer's entire pizza order, including all pizzas,
           total cost, and payment status.

Dependencies:
    - Pizza class (imported from the same package)
"""
from .pizza import Pizza 

# Represents a customer's order, consisting of one or more pizzas.
class Order:
    # Initialize an empty order.
    def __init__(self):
        #Initializes a customer order
        self.pizzas = []
        #initialize order cost
        self.total_cost = 0
        #initialize status of the order
        self.paid = False
    # Return a human-readable string representation of the order, listing all pizzas with their details.
    def __str__(self):
        pizza_descriptions = "\n".join(pizza.__str__() for pizza in self.pizzas)
        return f"Customer Requested:\n{pizza_descriptions}"
    
    #input the customers order for a given pizza
    def input_pizza(self,crust,sauce, cheese, toppings):
        #Initialize the pizza object and attach to the order
        pizza = Pizza(crust,sauce,cheese,toppings)
        self.pizzas.append(pizza)
        #Update cost
        self.total_cost += pizza.cost
    
    # Mark the order as paid.
    def order_paid(self):
        #Set order as paid once payment has been collected
        self.paid = True
    

