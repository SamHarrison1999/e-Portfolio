from Item import Item
from ShoppingCart import ShoppingCart

if __name__ == '__main__':
    item1 = Item('milk', 1.5, 1)
    item2 = Item('apple', 5, 0.75)
    item3 = Item('bread', 2, 2.25)
    cart = ShoppingCart()

    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)

    print(cart.get_total())
    print(cart.get_num_items())
    print(cart)
    print(cart.get_items())
