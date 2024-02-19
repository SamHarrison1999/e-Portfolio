from Inheritance.Deck import Deck


class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label


def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty


if __name__ == '__main__':
    hand = Hand('new hand')
    hand.cards
    hand.label

    deck = Deck()
    card = deck.pop_card()
    hand.add_card(card)
    print(hand)
    print(find_defining_class(hand, 'shuffle'))
