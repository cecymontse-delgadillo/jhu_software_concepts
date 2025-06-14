"""
test_pizza.py - Testing Pizza Module
-------------------------------------------------
Unit tests for the Pizza class.

Features: 
This test suite verifies:
- Correct initialization of Pizza objects
- Proper type and structure of Pizza attributes
- Correct cost calculation
- Correct string representation

Uses:
    - pytest fixtures
    - pytest markers for unit and order scope

"""
from src import Pizza
import pytest

# Fixture: Create a sample Pizza instance for reuse in tests.
@pytest.fixture
def example_init_pizza():
    return Pizza("Thin", ["Pesto", "Liv_Sauce"], "Mozzarella", ["Mushrooms", "Pepperoni"])

# Test: Pizza object initializes correctly with valid ingredients.
@pytest.mark.unit
@pytest.mark.pizza
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

# Test: __str__ returns the expected formatted string for the pizza.
@pytest.mark.unit
@pytest.mark.pizza
def test_pizza_str_function(example_init_pizza):
    #Test pizza should return a string containing the pizza and cost
    assert example_init_pizza.__str__() == "Crust: Thin, Sauce: ['Pesto', 'Liv_Sauce'], Cheese: Mozzarella, Toppings: ['Mushrooms', 'Pepperoni'], Cost: 18"

# Test: Cost calculation returns the correct total based on ingredients.
@pytest.mark.unit
@pytest.mark.pizza
def test_pizza_cost(example_init_pizza):
    #Test return of correct cost for an input pizza
    assert example_init_pizza.cost == 18