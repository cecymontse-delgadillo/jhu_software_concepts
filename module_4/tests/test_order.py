"""
test_order.py - Testing Order Module
-------------------------------------------------
Unit tests for the Order class.

Features: 

This test suite verifies:
- Order initializes correctly with no pizzas
- Adding pizzas updates the list and total cost
- String representation of the order includes all pizzas
- Payment status updates properly

Uses:
    - pytest fixtures
    - pytest markers for unit scope

"""
from src import Order
import pytest

# Fixture: Create an empty Order instance for testing.
@pytest.fixture
def example_init_order():
    return Order()

# Fixture: Create an Order with one pizza for testing.
@pytest.fixture
def example_simple_order():
    order_1 = Order()
    order_1.input_pizza("Thin", ["Pesto", "Liv_Sauce"], "Mozzarella", ["Mushrooms", "Pepperoni"])
    return order_1


# Fixture: Create an Order with two pizzas for testing.
@pytest.fixture
def example_complex_order():
    order_1 = Order()
    order_1.input_pizza("Thin", ["Pesto", "Liv_Sauce"], "Mozzarella", ["Mushrooms", "Pepperoni"])
    order_1.input_pizza("Thick", ["Pesto", "Liv_Sauce", "Marinara"], "Mozzarella", ["Mushrooms", "Pepperoni", "Pineapple"])
    return order_1


# Test: Order initializes correctly with default values.
@pytest.mark.unit
@pytest.mark.order
@pytest.mark.parametrize("attr, expected_result", [
    ("pizzas",[]),
    ("total_cost",0),
    ("paid",False)
])
def test_order_init_function(example_init_order, attr, expected_result):
    assert getattr(example_init_order, attr) == expected_result

# Test: __str__ returns a string listing all pizzas in the order.
@pytest.mark.unit
@pytest.mark.order
@pytest.mark.parametrize("fixture_funct, expected_result", [
    ("example_simple_order","Customer Requested:\n"
        "Crust: Thin, Sauce: ['Pesto', 'Liv_Sauce'], Cheese: Mozzarella, Toppings: ['Mushrooms', 'Pepperoni'], Cost: 18"),
    ("example_complex_order","Customer Requested:\n"
        "Crust: Thin, Sauce: ['Pesto', 'Liv_Sauce'], Cheese: Mozzarella, Toppings: ['Mushrooms', 'Pepperoni'], Cost: 18\n"
        "Crust: Thick, Sauce: ['Pesto', 'Liv_Sauce', 'Marinara'], Cheese: Mozzarella, Toppings: ['Mushrooms', 'Pepperoni', 'Pineapple'], Cost: 22"),
])
def test_order_str_function(request, fixture_funct,expected_result):
    # Test order should return a string containing customer full order and cost
    order = request.getfixturevalue(fixture_funct)
    assert order.__str__() == expected_result

@pytest.mark.unit
@pytest.mark.order
@pytest.mark.parametrize("fixture_funct, expected_result", [
    ("example_init_order",0),
    ("example_complex_order", 40),
])

# Test: Testing input_pizza also updates total_cost. 
@pytest.mark.unit
@pytest.mark.order
def test_input_pizza_cost(request, fixture_funct,expected_result):
    #Test method should update cost
    order = request.getfixturevalue(fixture_funct)
    assert order.total_cost == expected_result

# Test: Calling order_paid() sets the paid flag to True.
@pytest.mark.unit
@pytest.mark.order
def test_order_paid_function(example_init_order):
    #Test method should update paid to true
    assert example_init_order.paid is False
    example_init_order.order_paid()
    assert example_init_order.paid is True