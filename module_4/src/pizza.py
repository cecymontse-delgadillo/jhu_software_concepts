class Pizza:
    PRICES = {
        "crust": {"THIN": 5, "THICK": 6, "GLUTEN_FREE": 8},
        "toppings": {"PINEAPLE": 1, "PEPPERONI":2, "MUSHROOMS": 3},
        "sauce": {"MARINARA": 2, "PESTO": 3, "LIV_SAUCE": 5},
        "cheese": {"MOZZARELLA":0}   
    }

    """
    Initializes a Pizza object.

    :param crust: str - Only one crust allowed
    :param sauce: str or list - At least one sauce required
    :param cheese: str - Optional, but assumed to be one type
    :param toppings: str or list - At least one topping required
    """
    def __init__(self,crust,sauce,cheese,toppings):
        #Initiatizes Pizza
        #Set Pizza variables
        self.crust = self._validate_single("crust", crust)
        self.sauce = self._validate_multiple("sauce", sauce, required=True)
        self.cheese = self._validate_single("cheese", cheese)
        self.toppings = self._validate_multiple("toppings", toppings, required=True)
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
            cost = self.PRICES["crust"][str(self.crust).upper()]
            cost += sum(self.PRICES["sauce"][str(s).upper()] for s in self.sauce)
            cost += self.PRICES["cheese"][str(self.cheese).upper()]
            cost += sum(self.PRICES["toppings"][str(t).upper()] for t in self.toppings) 
            return cost                 
        except Exception as e:
             print(e)
    
    def _validate_single(self, category, item):
        if str(item).upper() not in self.PRICES[category]:
            raise ValueError(f"Invalid {category}: '{item}'")
        return item

    def _validate_multiple(self, category, items, required=False):
        if isinstance(items, str):
            items = [items]
        if required and not items:
            raise ValueError(f"At least one {category} must be selected.")
        for item in items:
            if str(item).upper() not in self.PRICES[category]:
                raise ValueError(f"Invalid {category}: '{item}'")
        return items

if __name__ == "__main__":
    pizza1= Pizza("Thin", ["Pesto", "Liv_Sauce"], "Mozzarella", ["Mushrooms", "Pepperoni"])
    pizza1.__str__()