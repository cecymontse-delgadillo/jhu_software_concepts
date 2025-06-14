"""
order.py - Order Model
-------------------------------------------------
This module defines the Order class, which manages a customer's pizza order.
An Order can contain multiple Pizza instances, tracks the total cost,
and keeps track of whether payment has been made.

Classes:
    Order: Represents a customer's entire pizza order, including all pizzas,
           total cost, and payment status.

Dependencies:
    - :py:class:`Pizza` (imported from the same package)
"""

from .pizza import Pizza


class Order:
    """
    Represents a customer's order, consisting of one or more pizzas.
    """

    def __init__(self):
        """
        Initialize an empty order.

        :pizzas:
            Empty List of :py:class:`Pizza` objects.
        :total_cost: float
            Cost 0 for init.
        :paid: bool
            The payment status of the order -Set to False.
        """
        self.pizzas = []
        self.total_cost = 0
        self.paid = False

    def __str__(self):
        """
        Return a human-readable string representation of the order,
        listing all pizzas with their details.

        Returns
        -------
        str
            A string describing the customer's order.
        """
        pizza_descriptions = "\n".join(str(pizza) for pizza in self.pizzas)
        return f"Customer Requested:\n{pizza_descriptions}"

    def input_pizza(self, crust, sauce, cheese, toppings):
        """Add a pizza to the order.

        :param crust: The type of crust for the pizza.
        :type crust: str
        :param sauce: The type of sauce for the pizza.
        :type sauce: list of str
        :param cheese: The type of cheese for the pizza.
        :type cheese: str
        :param toppings: The list of toppings for the pizza.
        :type toppings: list of str
        """
        # Create a new Pizza object and add it to the list
        pizza = Pizza(crust, sauce, cheese, toppings)
        self.pizzas.append(pizza)
        # Update the total cost
        self.total_cost += pizza.cost

    def order_paid(self):
        """
        Mark the order as paid.

        Sets the :py:attr:`paid` attribute to ``True``.
        """
        self.paid = True