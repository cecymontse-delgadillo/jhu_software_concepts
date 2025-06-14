"""
test_order.py - Testing Order Module
-------------------------------------------------
Unit tests for the Order class.

This test suite verifies:
- Order initializes correctly with no pizzas.
- Adding pizzas updates the list and total cost.
- String representation of the order includes all pizzas.
- Payment status updates properly.

Uses
----
- pytest fixtures
- pytest markers for unit scope
"""

from src import Order
import pytest


@pytest.fixture
def example_init_order():
    """
    Fixture: Create an empty Order instance for testing.

    Returns
    -------
    Order
        An empty Order instance.
    """
    return Order()


@pytest.fixture
def example_simple_order():
    """
    Fixture: Create an Order with one pizza for testing.

    Returns
    -------
    Order
        An Order instance with one pizza.
    """
    order_1 = Order()
    order_1.input_pizza("Thin", ["Pesto", "Liv_Sauce"], "Mozzarella", ["Mushrooms", "Pepperoni"])
    return order_1


@pytest.fixture
def example_complex_order():
    """
    Fixture: Create an Order with two pizzas for testing.

    Returns
    -------
    Order
        An Order instance with two pizzas.
    """
    order_1 = Order()
    order_1.input_pizza("Thin", ["Pesto", "Liv_Sauce"], "Mozzarella", ["Mushrooms", "Pepperoni"])
    order_1.input_pizza("Thick", ["Pesto", "Liv_Sauce", "Marinara"], "Mozzarella",
                        ["Mushrooms", "Pepperoni", "Pineapple"])
    return order_1


@pytest.mark.unit
@pytest.mark.order
@pytest.mark.parametrize(
    "attr, expected_result",
    [
        ("pizzas", []),
        ("total_cost", 0),
        ("paid", False)
    ]
)
def test_order_init_function(example_init_order, attr, expected_result):
    """
    Test that Order initializes correctly with default values.

    Parameters
    ----------
    example_init_order : Order
        Fixture providing an empty Order.
    attr : str
        Attribute name to check.
    expected_result : object
        Expected value of the attribute.
    """
    assert getattr(example_init_order, attr) == expected_result


@pytest.mark.unit
@pytest.mark.order
@pytest.mark.parametrize(
    "fixture_funct, expected_result",
    [
        (
            "example_simple_order",
            "Customer Requested:\n"
            "Crust: Thin, Sauce: ['Pesto', 'Liv_Sauce'], Cheese: Mozzarella, "
            "Toppings: ['Mushrooms', 'Pepperoni'], Cost: 18"
        ),
        (
            "example_complex_order",
            "Customer Requested:\n"
            "Crust: Thin, Sauce: ['Pesto', 'Liv_Sauce'], Cheese: Mozzarella, "
            "Toppings: ['Mushrooms', 'Pepperoni'], Cost: 18\n"
            "Crust: Thick, Sauce: ['Pesto', 'Liv_Sauce', 'Marinara'], Cheese: Mozzarella, "
            "Toppings: ['Mushrooms', 'Pepperoni', 'Pineapple'], Cost: 22"
        ),
    ]
)
def test_order_str_function(request, fixture_funct, expected_result):
    """
    Test that __str__ returns a string listing all pizzas in the order.

    Parameters
    ----------
    request : FixtureRequest
        The pytest request object to get fixtures by name.
    fixture_funct : str
        Name of the fixture providing an Order.
    expected_result : str
        Expected string representation.
    """
    order = request.getfixturevalue(fixture_funct)
    assert str(order) == expected_result


@pytest.mark.unit
@pytest.mark.order
@pytest.mark.parametrize(
    "fixture_funct, expected_result",
    [
        ("example_init_order", 0),
        ("example_complex_order", 40),
    ]
)
def test_input_pizza_cost(request, fixture_funct, expected_result):
    """
    Test that adding pizzas updates the total cost correctly.

    Parameters
    ----------
    request : FixtureRequest
        The pytest request object to get fixtures by name.
    fixture_funct : str
        Name of the fixture providing an Order.
    expected_result : int
        Expected total cost of the order.
    """
    order = request.getfixturevalue(fixture_funct)
    assert order.total_cost == expected_result


@pytest.mark.unit
@pytest.mark.order
def test_order_paid_function(example_init_order):
    """
    Test that calling order_paid() sets the paid flag to True.

    Parameters
    ----------
    example_init_order : Order
        Fixture providing an empty Order.
    """
    assert example_init_order.paid is False
    example_init_order.order_paid()
    assert example_init_order.paid is True
