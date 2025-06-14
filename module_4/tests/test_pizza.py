"""
test_pizza.py - Testing Pizza Module
-------------------------------------------------
Unit tests for the Pizza class.

This test suite verifies:
- Correct initialization of Pizza objects.
- Proper type and structure of Pizza attributes.
- Correct cost calculation.
- Correct string representation.

Uses
----
- pytest fixtures
- pytest markers for unit and pizza scope
"""

from src import Pizza
import pytest


@pytest.fixture
def example_init_pizza():
    """
    Fixture: Create a sample Pizza instance for reuse in tests.

    Returns
    -------
    Pizza
        A Pizza instance with known ingredients.
    """
    return Pizza("Thin", ["Pesto", "Liv_Sauce"], "Mozzarella", ["Mushrooms", "Pepperoni"])


@pytest.mark.unit
@pytest.mark.pizza
def test_pizza_init_function(example_init_pizza):
    """
    Test that a Pizza object initializes correctly with valid ingredients
    and that its attributes have the correct types and values.

    Parameters
    ----------
    example_init_pizza : Pizza
        Fixture providing a sample Pizza instance.
    """
    assert isinstance(example_init_pizza, Pizza)

    # Test crust is a string.
    assert isinstance(example_init_pizza.crust, str)

    # Test sauce is a list of strings.
    assert isinstance(example_init_pizza.sauce, list)
    assert all(isinstance(s, str) for s in example_init_pizza.sauce)

    # Test cheese is a string.
    assert isinstance(example_init_pizza.cheese, str)

    # Test toppings is a list of strings.
    assert isinstance(example_init_pizza.toppings, list)
    assert all(isinstance(t, str) for t in example_init_pizza.toppings)

    # Test cost is computed and non-zero.
    assert example_init_pizza.cost != 0


@pytest.mark.unit
@pytest.mark.pizza
def test_pizza_str_function(example_init_pizza):
    """
    Test that __str__ returns the expected formatted string for the pizza.

    Parameters
    ----------
    example_init_pizza : Pizza
        Fixture providing a sample Pizza instance.
    """
    expected = (
        "Crust: Thin, Sauce: ['Pesto', 'Liv_Sauce'], Cheese: Mozzarella, "
        "Toppings: ['Mushrooms', 'Pepperoni'], Cost: 18"
    )
    assert str(example_init_pizza) == expected


@pytest.mark.unit
@pytest.mark.pizza
def test_pizza_cost(example_init_pizza):
    """
    Test that the cost calculation returns the correct total
    based on the specified ingredients.

    Parameters
    ----------
    example_init_pizza : Pizza
        Fixture providing a sample Pizza instance.
    """
    assert example_init_pizza.cost == 18
