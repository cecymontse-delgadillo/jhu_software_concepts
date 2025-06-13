from src import Order
import pytest


@pytest.fixture
def example_complex_order():
    order_1 = Order()
    order_1.input_pizza("thin", ["pesto"], "mozzarella", ["mushrooms"])
    order_1.input_pizza("thick", ["marinara"], "mozzarella", ["mushrooms"])
    return order_1

@pytest.fixture
def example_complex_order_two():
    order_2 = Order()
    order_2.input_pizza("gluten_free", ["marinara"], "mozzarella", ["pineapple"])
    order_2.input_pizza("thin", ["liv_sauce", "pesto"], "mozzarella", ["mushrooms","pepperoni"])
    return order_2

@pytest.mark.integration
@pytest.mark.order
@pytest.mark.parametrize("fixture_funct, expected_result", [
   ("example_complex_order","Customer Requested:\n"
        "Crust: thin, Sauce: ['pesto'], Cheese: mozzarella, Toppings: ['mushrooms'], Cost: 11\n"
        "Crust: thick, Sauce: ['marinara'], Cheese: mozzarella, Toppings: ['mushrooms'], Cost: 11"),
    ("example_complex_order_two","Customer Requested:\n"
        "Crust: gluten_free, Sauce: ['marinara'], Cheese: mozzarella, Toppings: ['pineapple'], Cost: 11\n"
        "Crust: thin, Sauce: ['liv_sauce', 'pesto'], Cheese: mozzarella, Toppings: ['mushrooms', 'pepperoni'], Cost: 18")
])
def test_order_str_function(request, fixture_funct,expected_result):
    # Test order should return a string containing customer full order and cost
    order = request.getfixturevalue(fixture_funct)
    assert order.__str__() == expected_result