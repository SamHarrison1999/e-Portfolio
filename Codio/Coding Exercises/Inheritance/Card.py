class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


if __name__ == '__main__':
    queen_of_diamonds = Card(1, 12)
    card1 = Card(2, 11)
    print(card1)
    print(queen_of_diamonds < card1)


class Time(object):
    def __init__(self, hour=0, minute=0):
        self.hour = hour
        self.minute = minute

    def __lt__(self, other):
        return (self.hour, self.minute) < (other.hour, other.minute)