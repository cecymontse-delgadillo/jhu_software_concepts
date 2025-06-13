# main.py

from src.order import Order
from src.pizza import Pizza




if __name__ == "__main__":
    order = Order()
    order.input_pizza("thin", ["pesto"], "mozzarella", ["mushrooms"])
    order.input_pizza("thick", ["marinara"], "mozzarella", ["mushrooms"])
    print(order.__str__())
    order_2 = Order()
    order_2.input_pizza("gluten_free", ["marinara"], "mozzarella", ["pineapple"])
    order_2.input_pizza("thin", ["liv_sauce", "pesto"], "mozzarella", ["mushrooms","pepperoni"])
    print(order_2.__str__())