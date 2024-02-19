import random

from Inheritance.Card import Card
from Inheritance.Hand import *


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def sort(self):
        self.cards.sort()

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, number_of_hands, number_of_cards):
        hand_list = []
        for hand in range(number_of_hands):
            hand = Hand()
            self.move_cards(hand, number_of_cards)
            hand_list.append(hand)
        return hand_list


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    hand = Hand()
    print(find_defining_class(hand, 'shuffle'))

    deck.move_cards(hand, 5)
    hand.sort()
    print(hand)
    print(deck)
