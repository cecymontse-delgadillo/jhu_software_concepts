from src import Order
import pytest

@pytest.fixture
def example_init_order():
    return Order()

@pytest.fixture
def example_simple_order():
    order_1 = Order()
    order_1.input_pizza("Thin", ["Pesto", "Liv_Sauce"], "Mozzarella", ["Mushrooms", "Pepperoni"])
    return order_1

@pytest.fixture
def example_complex_order():
    order_1 = Order()
    order_1.input_pizza("Thin", ["Pesto", "Liv_Sauce"], "Mozzarella", ["Mushrooms", "Pepperoni"])
    order_1.input_pizza("Thick", ["Pesto", "Liv_Sauce", "Marinara"], "Mozzarella", ["Mushrooms", "Pepperoni", "Pineapple"])
    return order_1

@pytest.mark.unit
@pytest.mark.parametrize("attr, expected_result", [
    ("pizzas",[]),
    ("total_cost",0),
    ("paid",False)
])
def test_order_init_function(example_init_order, attr, expected_result):
    assert getattr(example_init_order, attr) == expected_result

@pytest.mark.unit
@pytest.mark.parametrize("fixture_funct, expected_result", [
    ("example_simple_order","Customer Requested:\nCrust: Thin, Sauce: ['Pesto', 'Liv_Sauce'], Cheese: Mozzarella, Toppings: ['Mushrooms', 'Pepperoni'], Cost: 18"),
    ("example_complex_order","Customer Requested:\nCrust: Thin, Sauce: ['Pesto', 'Liv_Sauce'], Cheese: Mozzarella, Toppings: ['Mushrooms', 'Pepperoni'], Cost: 18 \nCrust: Thick, Sauce: ['Pesto', 'Liv_Sauce', 'Marinara'], Cheese: Mozzarella, Toppings: ['Mushrooms', 'Pepperoni', 'Pineapple'], Cost: 22"),
])
def test_order_str_function(request, fixture_funct,expected_result):
    # Test order should return a string containing customer full order and cost
    order = request.getfixturevalue(fixture_funct)
    assert order.__str__() == expected_result

@pytest.mark.unit
@pytest.mark.parametrize("fixture_funct, expected_result", [
    ("example_init_order",0),
    ("example_complex_order", 40),
])

@pytest.mark.unit
def test_input_pizza_cost(request, fixture_funct,expected_result):
    #Test method should update cost
    order = request.getfixturevalue(fixture_funct)
    assert order.total_cost == expected_result

@pytest.mark.unit
def test_order_paid_function(example_init_order):
    #Test method should update paid to true
    assert example_init_order.paid is False
    example_init_order.order_paid()
    assert example_init_order.paid is True