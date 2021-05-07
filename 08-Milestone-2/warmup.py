"""
Card War Game
"""
# Card
# Suit, Rank, Values
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    """
    This class is for defining a single Card
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        """ this function returns the Name of card """
        return self.rank + " of " + self.suit

    def shuffle(self):
        """ This function shuffle all the cards """
        return self.rank



twohearts = Card('Hearts', 'Two')
threeclub = Card('Club', 'Three')
print(twohearts)
print(twohearts.suit)
print(twohearts.rank)
print(twohearts.value)
print(threeclub)
print(threeclub.suit)
print(threeclub.rank)
print(threeclub.value)

if threeclub.value > twohearts.value:
    print('player 1 wins')
