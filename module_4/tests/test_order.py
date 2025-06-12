from src import Order

def test_order_init_function():
    order_1 = Order()
    #Assert order should include an empty list of pizza objects
    assert order_1.pizzas == []
    #Assert order should have a zero cost until an order is input
    assert order_1.total_cost == 0
    #Assert order should not have yet been paid
    assert order_1.status == False

def test_order_str_function():
    # Test order should return a string containing customer full order and cost
    order_1= Order()
    order_1.input_pizza("Thin", ["Pesto", "Liv_Sauce"], "Mozzarella", ["Mushrooms", "Pepperoni"])
    assert order_1.__str__() == "Customer Requested:\nCrust: Thin, Sauce: ['Pesto', 'Liv_Sauce'], Cheese: Mozzarella, Toppings: ['Mushrooms', 'Pepperoni'], Cost: 18"

def test_input_pizza_cost():
    #Test method should update cost
    order_1= Order()
    assert order_1.total_cost == 0 
    order_1.input_pizza("Thin", ["Pesto", "Liv_Sauce"], "Mozzarella", ["Mushrooms", "Pepperoni"])
    assert order_1.total_cost == 18

def test_order_paid_function():
    #Test method should update paid to true
    order_1= Order()
    assert order_1.paid == False
    order_1.order_paid()
    assert order_1.paid == True