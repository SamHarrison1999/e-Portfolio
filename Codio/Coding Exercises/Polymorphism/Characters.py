class Characters:
    def __init__(self, phrases):
        self.phrases = phrases

    def total_characters(self):
        total = 0
        for phrase in self.phrases:
            total += len(phrase)
        return total
    
    def __lt__(self, other):
        return self.total_characters() < other.total_characters()

    def __gt__(self, other):
        return self.total_characters() > other.total_characters()

    def __eq__(self, other):
        return self.total_characters() == other.total_characters()


if __name__ == '__main__':
    sample_phrases1 = ['cat in the hat', 'green eggs and ham', 'the lorax']
    sample_phrases2 = ['the taming of the shrew', 'hamlet', 'othello']

    c1 = Characters(sample_phrases1)
    c2 = Characters(sample_phrases2)
    print(c1 > c2)  # prints 'True'
    print(c1 < c2)  # prints 'False'
    print(c1 == c1)  # prints 'True'
