class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.subtotal = 0

    def calculate_subtotal(self):
        self.subtotal = self.price * self.quantity

    def get_subtotal(self):
        return self.subtotal

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity}, {self.subtotal})"

