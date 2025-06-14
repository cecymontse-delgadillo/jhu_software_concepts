"""
pizza.py - Pizza Module
-------------------------------------------------
This module defines the Pizza class, which models a customizable pizza.
It supports different crusts, sauces, cheeses, and toppings. Each pizza's
ingredients are validated and its total cost is computed automatically.

Classes:
    Pizza: Represents a single pizza with specified ingredients and cost.

"""

# Class that presents a customizable pizza with crust, sauce(s), cheese, and toppings.
# Calculates total price based on selected ingredients.
class Pizza:
    # Static price list for all ingredients
    PRICES = {
        "crust": {"THIN": 5, "THICK": 6, "GLUTEN_FREE": 8},
        "toppings": {"PINEAPPLE": 1, "PEPPERONI":2, "MUSHROOMS": 3},
        "sauce": {"MARINARA": 2, "PESTO": 3, "LIV_SAUCE": 5},
        "cheese": {"MOZZARELLA":0}   
    }
    # Initialize a Pizza with specified ingredients. Validate ingredients and compute the total cost.
    def __init__(self,crust,sauce,cheese,toppings):
        #Initiatizes Pizza
        #Set Pizza variables
        self.crust = self._validate_single("crust", crust)
        self.sauce = self._validate_multiple("sauce", sauce, required=True)
        self.cheese = self._validate_single("cheese", cheese)
        self.toppings = self._validate_multiple("toppings", toppings, required=True)
        #Set cost to create
        self.cost = self.cost()
    
    # Return a human-readable string representation of the pizza, listing ingredients and total cost.
    def __str__(self):
        #Print a pizza
        #Print the cost of that pizza
        return (f"Crust: {self.crust}, Sauce: {self.sauce}, Cheese: {self.cheese}, Toppings: {self.toppings}, Cost: {self.cost}")

    #Determine the cost of a pizza   
    def cost(self):
        try:
            # Add cost of crust 
            cost = self.PRICES["crust"][str(self.crust).upper()]
            cost += sum(self.PRICES["sauce"][str(s).upper()] for s in self.sauce)
            cost += self.PRICES["cheese"][str(self.cheese).upper()]
            cost += sum(self.PRICES["toppings"][str(t).upper()] for t in self.toppings) 
            return cost                 
        except Exception as e:
             print(e)


    # Validate a single ingredient against the PRICES list.
    def _validate_single(self, category, item):
        if str(item).upper() not in self.PRICES[category]:
            raise ValueError(f"Invalid {category}: '{item}'")
        return item

    # Validate multiple ingredients (sauces or toppings).
    def _validate_multiple(self, category, items, required=False):
        if isinstance(items, str):
            items = [items]
        if required and not items:
            raise ValueError(f"At least one {category} must be selected.")
        for item in items:
            if str(item).upper() not in self.PRICES[category]:
                raise ValueError(f"Invalid {category}: '{item}'")
        return items
    
