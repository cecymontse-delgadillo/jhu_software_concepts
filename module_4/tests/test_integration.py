"""
test_integration.py - Integration Testing Module
-------------------------------------------------
Integration tests for the Order class with multiple Pizza instances.

This test suite verifies:
- Correct handling of complex orders containing multiple pizzas.
- Correct string representation including all pizzas and their costs.

Uses
----
- pytest fixtures
- pytest markers for integration and order scope
"""

from src import Order
import pytest


@pytest.fixture
def example_complex_order():
    """
    Fixture: Create an Order with two simple pizzas for integration testing.

    Returns
    -------
    Order
        An Order instance containing two pizzas.
    """
    order_1 = Order()
    order_1.input_pizza("thin", ["pesto"], "mozzarella", ["mushrooms"])
    order_1.input_pizza("thick", ["marinara"], "mozzarella", ["mushrooms"])
    return order_1


@pytest.fixture
def example_complex_order_two():
    """
    Fixture: Create an Order with two pizzas having different crusts and toppings.

    Returns
    -------
    Order
        An Order instance containing two pizzas with varying ingredients.
    """
    order_2 = Order()
    order_2.input_pizza("gluten_free", ["marinara"], "mozzarella", ["pineapple"])
    order_2.input_pizza("thin", ["liv_sauce", "pesto"], "mozzarella", ["mushrooms", "pepperoni"])
    return order_2


@pytest.mark.integration
@pytest.mark.order
@pytest.mark.parametrize(
    "fixture_funct, expected_result",
    [
        (
            "example_complex_order",
            "Customer Requested:\n"
            "Crust: thin, Sauce: ['pesto'], Cheese: mozzarella, Toppings: ['mushrooms'], Cost: 11\n"
            "Crust: thick, Sauce: ['marinara'], Cheese: mozzarella, Toppings: ['mushrooms'], Cost: 11",
        ),
        (
            "example_complex_order_two",
            "Customer Requested:\n"
            "Crust: gluten_free, Sauce: ['marinara'], Cheese: mozzarella, Toppings: ['pineapple'], Cost: 11\n"
            "Crust: thin, Sauce: ['liv_sauce', 'pesto'], Cheese: mozzarella, Toppings: ['mushrooms', 'pepperoni'], Cost: 18",
        ),
    ],
)
def test_order_str_function(request, fixture_funct, expected_result):
    """
    Test that the Order's string representation includes all pizzas and
    their details for complex orders.

    Parameters
    ----------
    request : _pytest.fixtures.FixtureRequest
        Pytest's built-in request object to access fixtures dynamically.
    fixture_funct : str
        Name of the fixture to use for testing.
    expected_result : str
        Expected string representation of the order.
    """
    order = request.getfixturevalue(fixture_funct)
    assert str(order) == expected_result
