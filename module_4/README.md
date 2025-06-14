# Pytest and Sphinx: Python Pizza Ordering System

A simple Python system to build pizzas with your choice of crust, sauces, cheese, and toppings — add them to an order, calculate costs, and test it all with pytest. Documentation generated with Sphinx. 

## Project Structure
.
├── src/
│   ├── __init__.py     # Initializes the module, and imports Order and Pizza
│   ├── pizza.py        # Defines the Pizza class: ingredients & pricing
│   ├── order.py        # Defines the Order class: manages multiple pizzas & payment status
├── tests/
│   ├── __init__.py     # Initializes the module.
│   ├── test_pizza.py   # Unit tests for Pizza
│   ├── test_order.py   # Unit tests for Order
│   ├── test_order_integration.py  # Integration tests for Order + multiple pizzas
├── pytest.ini           # A pytest.ini to register your custom markers
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation


## Features
- Customizable Pizza class
- Cost calculated from validated ingredients
- Order class for multiple pizzas + total cost tracking
- Payment status
- Complete test coverage with pytest (unit & integration)


##  Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/cecymontse-delgadillo/jhu_software_concepts.git
cd jhu_software_concepts/module_4/
```
### 2. Install Python dependencies

This project uses the standard library only, but ensure your environment includes:
```bash
    pip install -r requirements.txt
```
## Usage

```python
from src.order import Order

order = Order()
order.input_pizza("thin", ["marinara"], "mozzarella", ["pineapple", "pepperoni"])
order.input_pizza("thick", ["pesto"], "mozzarella", ["mushrooms"])

print(order)
print(f"Total Cost: {order.total_cost}")

order.order_paid()
print(f"Paid: {order.paid}")

```

## Running Tests

### 1. Run all tests Order and Pizza (unit + integration):
```bash
pytest

```

### 2. Run all tests Order:
```bash
pytest -m order -vv

```

### 3. Run all tests Pizza:
```bash
pytest -m pizza -vv

```
### 4. Run all unit tests:
```bash
pytest -m unit -vv

```

### 5. Run all integration tests:
```bash
pytest -m integration -vv

```

## What is tested?
| File                        | Scope       | What it verifies                                                    |
| --------------------------- | ----------- | ------------------------------------------------------------------- |
| `test_pizza.py`             | Unit        | `Pizza` init, ingredient validation, string output, non-zero cost    |
| `test_order.py`             | Unit        | `Order` init, `input_pizza` updates cost, `__str__`, `order_paid()` |
| `test_order_integration.py` | Integration | Complex orders with multiple pizzas and cost correctness            |



# Contact
cdelga15@jhu.edu