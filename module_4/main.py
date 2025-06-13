# main.py

from src.order import Order
from src.pizza import Pizza




if __name__ == "__main__":
    order = Order()
    order.input_pizza("Thick", ["Pesto", "Liv_Sauce", "Marinara"], "Mozzarella", ["Mushrooms", "Pepperoni", "Pineapple"])
    order.input_pizza("Thin", ["Pesto", "Liv_Sauce", "Marinara"], "Mozzarella", ["Mushrooms", "Pepperoni", "Pineapple"])
    print(order.__str__())