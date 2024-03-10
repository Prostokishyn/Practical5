class Order:
    def __init__(self):
        self._products = []
    def add_product(self, product_name, quantity, price):
        self._products.append((product_name, quantity, price))
    def total_cost(self):
        total = 0
        for product in self._products:
            total += product[1] * product[2]
        return total

class Customer:
    def __init__(self, name):
        self.name = name
    def add_product(self, order, product_name, quantity, price):
        order.add_product(product_name, quantity, price)


class OrderProcessor:
    def process_order(self, order):
        total = order.total_cost()
        print("Загальна вартість", total)
        
order_processor = OrderProcessor()
customer = Customer("Альоша")
order = Order()
customer.add_product(order, "Ручка", 1, 10)
customer.add_product(order, "Зошит", 3, 21)
order_processor.process_order(order)