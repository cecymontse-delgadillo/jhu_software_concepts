class Pizza:
    TOPPINGS_CATALOG = {
        "Pineaple": 1,
        "Pepperoni":2,
        "Mushrooms": 3
    }
    SAUCE_CATALOG = {
        "Marinara": 2,
        "Pesto":3,
        "Liv_Sauce": 5
    }
    CRUST_CATALOG ={
        "Thin": 5,
        "Thick": 6,
        "Gluten Free": 8
    }
    CHEESE_CATALOG = {
        "Mozzarella":0
    }

    #Pizza objects and associated cost
    def __init__(self,crust,sauce,cheese,toppings):
        #Initiatizes Pizza
        #Set Pizza variables
        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings
        #Set cost to create
        self.cost = self.cost()
    
    def __str__(self):
        #Print a pizza
        #Print the cost of that pizza
        print(f" Crust: {self.crust}, Sauce: {self.sauce}, Cheese: {self.cheese}, Toppings: {self.toppings}, Cost: {self.cost}")

    
    def cost(self):
        #Determine the cost of a pizza
        try:
            # Add cost of crust 
            cost = self.CRUST_CATALOG[(self.crust)] if self.CRUST_CATALOG[self.crust] else 0
            cost += cost + self.CHEESE_CATALOG[self.cheese] if self.CHEESE_CATALOG[self.cheese] else 0
            for item in self.sauce:
                 cost += cost + self.SAUCE_CATALOG[self.sauce] if self.SAUCE_CATALOG[self.sauce] else 0
            for item in self.toppings:
                 cost += cost + self.TOPPINGS_CATALOG[self.toppings] if self.TOPPINGS_CATALOG[self.toppings] else 0  
            return cost                 
        except Exception as e:
             print(e)

if __name__ == "__main__":
    pizza1= Pizza("Thin", ["Pesto", "Liv_sauce"], "Mozzarella", ["Mushrooms", "Pepperoni"])
    pizza1.__str__()