"""
    This class stores all the information
    about each card inside a single object.

"""


class Card:

    def __init__(self, index, suit):
        """
        Each card gets an ID and a suit so that a deck of all possible
        cards can be implemented
        id_to_name properties enables the easy conversion from ID to name
        """

        self.id = index
        self.suit = suit
        self. id_to_name = {2: 'two', 3: 'three', 4: 'four', 5: 'five',
                            6: 'six', 7: 'seven', 8: 'eight',
                            9: 'nine', 10: 'ten', 11: 'jack',
                            12: 'queen', 13: 'king', 14: 'ace'
                            }
        self.suit_to_name ={'H': 'hearts', 'D': 'diamonds',
                            'C': 'clubs', 'S': 'spades'}
        self.name = str(self.id_to_name[index] + ' ' +
                        str(self.suit_to_name[suit]))





