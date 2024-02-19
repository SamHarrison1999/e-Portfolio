class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, item):
        self.items.append(item)
        self.calculate_total()

    def calculate_total(self):
        self.total = 0
        for item in self.items:
            item.calculate_subtotal()
            self.total += item.get_subtotal()

    def get_total(self):
        return self.total

    def get_num_items(self):
        return len(self.items)

    def get_items(self):
        return self.items

    def __str__(self):
        return f'The cart has {self.get_num_items()} items for a total of ${self.total}'