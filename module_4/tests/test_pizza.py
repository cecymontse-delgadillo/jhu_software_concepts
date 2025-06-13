from src import Pizza
import pytest

@pytest.fixture
def example_init_pizza():
    return Pizza("Thin", ["Pesto", "Liv_Sauce"], "Mozzarella", ["Mushrooms", "Pepperoni"])

@pytest.mark.unit
def test_pizza_init_function(example_init_pizza):
    #Test return an initialized pizza
    assert isinstance(example_init_pizza, Pizza)
    #Test pizza should have crust (str), sauce (list of str), cheese (str), toppings (list of str)
    assert isinstance(example_init_pizza.crust, str)
    assert isinstance(example_init_pizza.sauce, list)
    assert all(isinstance(s, str) for s in example_init_pizza.sauce)
    assert isinstance(example_init_pizza.cheese, str)
    assert isinstance(example_init_pizza.toppings, list)
    assert all(isinstance(s, str) for s in example_init_pizza.toppings)
    #Test pizza should return a non-zero cost
    assert example_init_pizza.cost != 0

@pytest.mark.unit
def test_pizza_str_function(example_init_pizza):
    #Test pizza should return a string containing the pizza and cost
    assert example_init_pizza.__str__() == "Crust: Thin, Sauce: ['Pesto', 'Liv_Sauce'], Cheese: Mozzarella, Toppings: ['Mushrooms', 'Pepperoni'], Cost: 18"

@pytest.mark.unit
def test_pizza_cost(example_init_pizza):
    #Test return of correct cost for an input pizza
    assert example_init_pizza.cost == 18