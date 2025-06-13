from src import Pizza

def test_pizza_init_function():
    #Test return an initialized pizza
    pizza_1= Pizza("Thin", ["Pesto", "Liv_Sauce"], "Mozzarella", ["Mushrooms", "Pepperoni"])
    assert isinstance(pizza_1, Pizza)
    #Test pizza should have crust (str), sauce (list of str), cheese (str), toppings (list of str)
    assert isinstance(pizza_1.crust, str)
    assert isinstance(pizza_1.sauce, list)
    assert all(isinstance(s, str) for s in pizza_1.sauce)
    assert isinstance(pizza_1.cheese, str)
    assert isinstance(pizza_1.toppings, list)
    assert all(isinstance(s, str) for s in pizza_1.toppings)
    #Test pizza should return a non-zero cost
    assert pizza_1.cost != 0

def test_pizza_str_function():
    #Test pizza should return a string containing the pizza and cost
    pizza_1= Pizza("Thin", ["Pesto", "Liv_Sauce"], "Mozzarella", ["Mushrooms", "Pepperoni"])
    assert pizza_1.__str__() == "Crust: Thin, Sauce: ['Pesto', 'Liv_Sauce'], Cheese: Mozzarella, Toppings: ['Mushrooms', 'Pepperoni'], Cost: 18"

def test_pizza_cost():
    #Test return of correct cost for an input pizza
    pizza_1= Pizza("Thick", ["Pesto", "Liv_Sauce", "Marinara"], "Mozzarella", ["Mushrooms", "Pepperoni", "Pineapple"])
    assert pizza_1.cost == 22