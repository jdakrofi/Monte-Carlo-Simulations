import random
import copy
from Card import Card
# from CheckScore import jacks_or_better_scorer

class deck:
    def __init__(self):
        """
            Creates a deck and stores it in an attribute
            Current hand of a player can be stored in final hand
        """
        self.deck = self.build_deck()
        self.final_hand = None

    def build_deck(self):
        """
            Creates all 52 cards by looping through all the suits
             and card values (by id).
        :return: deck
        """

        deck = []
        suits = ['H', 'D', 'C', 'S']
        for suit in suits:
            for idx in range(2, 15):
                deck.append(Card(idx, suit))
        return deck

    def shuffle(self):
        """
            Shuffles the cards randomly
        """
        random.shuffle(self.deck)

    def deal_five(self):
        """
            Hand stores the 5 cards given to a player
            remaining_cards stores the remaining 47 cards
        """
        self.hand = self.deck[:5]
        self.remaining_cards = self.deck[5:]

    def draw_cards(self, ids_to_hold=[], shuffle_remaining=False):
        """
            After dealing 5 cards this function is used to determine
            how many cards a player wants to hold from their hand.

            ids_to_hold stores the locations of the cards in the 5 card
            hand to be held. ids_to_holds = [0,2] keeps the first and
            third cards in a 5 card hand.

            cards from remaining_cards are used to replace the cards
            which will not be held.

            shuffle_remaining gives one the option to shuffle the
            remaining cards
        """
        new_hand = copy.copy(self.hand)
        remaining_cards = copy.copy(self.remaining_cards)

        if shuffle_remaining:
            random.shuffle(remaining_cards)

        for i, card in enumerate(new_hand):
            if i not in ids_to_hold:
                new_hand[i] = remaining_cards.pop(0)

        self.final_hand = new_hand

    def show_hand(self):
        """
            Prints a players hand
        """

        for c in self.hand:
            print(c.name)

    def show_remaining(self):
        """
            Prints remaining cards and uses set math to check that no card
            appears in both the hand the remaining cards
        """
        print(" ")
        print("--- REMAINING ---")
        for c in self.remaining_cards:
            print(c.name)

        print("--- check for intersections ---")
        print(set(self.hand) & set(self.remaining_cards))


"""cards = deck()
#cards.shuffle()
cards.deal_five()
cards.show_hand()
print("  ")
jb= jacks_or_better_scorer(cards.hand)
print(jb.score)
#cards.show_remaining()"""