"""
pizza.py - Pizza Module
-------------------------------------------------
This module defines the Pizza class, which models a customizable pizza.
It supports different crusts, sauces, cheeses, and toppings. Each pizza's
ingredients are validated and its total cost is computed automatically.

Classes
-------
:py:class:`Pizza`
    Represents a single pizza with specified ingredients and cost.
"""


class Pizza:
    """
    Represents a customizable pizza with crust, sauce(s), cheese, and toppings.
    Calculates total price based on selected ingredients.

    Attributes
    ----------
    :py:attr:`PRICES` : dict
        Static price list for all valid ingredients.
    :py:attr:`crust` : str
        The crust type for this pizza.
    :py:attr:`sauce` : list of str
        List of sauce(s) used on the pizza.
    :py:attr:`cheese` : str
        The cheese type for this pizza.
    :py:attr:`toppings` : list of str
        List of toppings added to the pizza.
    :py:attr:`cost` : float
        Total computed cost for this pizza.
    """

    PRICES = {
        "crust": {"THIN": 5, "THICK": 6, "GLUTEN_FREE": 8},
        "toppings": {"PINEAPPLE": 1, "PEPPERONI": 2, "MUSHROOMS": 3},
        "sauce": {"MARINARA": 2, "PESTO": 3, "LIV_SAUCE": 5},
        "cheese": {"MOZZARELLA": 0}
    }

    def __init__(self, crust, sauce, cheese, toppings):
        """
        Initialize a Pizza with specified ingredients. Ingredients are validated
        and the total cost is computed.

        :param crust: The crust type.
        :type crust: str
        :param sauce: One or more sauces.
        :type sauce: str or list of str
        :param cheese: The cheese type.
        :type cheese: str
        :param toppings: One or more toppings.
        :type toppings: str or list of str

        :raises ValueError: If an ingredient is invalid or required ingredients are missing.
        """

        self.crust = self._validate_single("crust", crust)
        self.sauce = self._validate_multiple("sauce", sauce, required=True)
        self.cheese = self._validate_single("cheese", cheese)
        self.toppings = self._validate_multiple("toppings", toppings, required=True)
        self.cost = self.pizza_cost()

    def __str__(self):
        """
        Return a human-readable string representation of the pizza.

        :returns: A string listing the pizza's ingredients and total cost.
        :rtype: str
        """
        return (f"Crust: {self.crust}, Sauce: {self.sauce}, Cheese: {self.cheese}, "
                f"Toppings: {self.toppings}, Cost: {self.cost}")

    def pizza_cost(self):
        """
        Calculate the total cost of the pizza based on selected ingredients.

        :returns: The total cost of the pizza.
        :rtype: float

        :raises Exception: If an ingredient is missing from the price list.
        """
        try:
            # Base cost: crust price
            cost = self.PRICES["crust"][str(self.crust).upper()]
            # Add sauces cost
            cost += sum(self.PRICES["sauce"][str(s).upper()] for s in self.sauce)
            # Add cheese cost
            cost += self.PRICES["cheese"][str(self.cheese).upper()]
            # Add toppings cost
            cost += sum(self.PRICES["toppings"][str(t).upper()] for t in self.toppings)
            return cost
        except Exception as e:
            print(e)

    def _validate_single(self, category, item):
        """
        Validate a single ingredient against the price list.

        :param category: The ingredient category ('crust', 'cheese').
        :type category: str
        :param item: The ingredient to validate.
        :type item: str

        :returns: The validated ingredient.
        :rtype: str

        :raises ValueError: If the ingredient is invalid.
        """
        if str(item).upper() not in self.PRICES[category]:
            raise ValueError(f"Invalid {category}: '{item}'")
        return item

    def _validate_multiple(self, category, items, required=False):
        """
        Validate multiple ingredients against the price list.

        :param category: The ingredient category ('sauce', 'toppings').
        :type category: str
        :param items: One or more ingredients to validate.
        :type items: str or list of str
        :param required: If True, at least one ingredient must be provided.
        :type required: bool, optional

        :returns: The validated list of ingredients.
        :rtype: list of str

        :raises ValueError: If any ingredient is invalid or required ingredients are missing.
        """
        if isinstance(items, str):
            items = [items]
        if required and not items:
            raise ValueError(f"At least one {category} must be selected.")
        for item in items:
            if str(item).upper() not in self.PRICES[category]:
                raise ValueError(f"Invalid {category}: '{item}'")
        return items
    
