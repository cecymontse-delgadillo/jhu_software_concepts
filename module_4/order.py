from pizza import Pizza

class Order:
    def __init__(self):
        #Initializes a customer order
        self.pizzas = []
        #initialize order cost
        self.total_cost = 0
        #initialize status of the order
        self.status = "Submitted"
    
    def __str__(self):
        pizza_descriptions = "\n".join(str(pizza) for pizza in self.pizzas)
        return f"Customer Requested:\n{pizza_descriptions}"
    
    #input the customers order for a given pizza
    def input_pizza(self,crust,sauce, cheese, toppings):
        #Initialize the pizza object and attach to the order
        pizza = Pizza(crust,sauce,cheese,toppings)
        self.pizzas.append(pizza)
        #Update cost
        self.total_cost += pizza.cost
    
    def order_paid(self):
        #Set order as paid once payment has been collected
        self.status = "Paid"
        