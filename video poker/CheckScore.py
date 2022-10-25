from collections import Counter


class jacks_or_better_scorer:
    def __init__(self, hand):
        """
              A hand is received and the following is checked:
            - whether the hand has 5 cards
            - the list of suits and ids in the hand
            - if the hand has any straights and pairs using ids
            - if the hand has any flushes using suits.
            - if there are any straight flushes
            The maximum payout is then calculated.
        """

        assert len(hand) == 5
        self.ids = [x.id for x in hand]
        self.suits = [x.suit for x in hand]
        pairs = self.check_for_pairs()
        flush = self.check_for_flush()
        straight = self.check_for_straight()
        straight_flush = self.check_straight_flush(straight, flush)
        self.score = max([pairs, flush, straight, straight_flush])

    def check_for_pairs(self):
        """
            Using the Counter object to check for 4 of a kind,
            full house, three of a kind, two pairs and
            one pair (but the id has to be bigger than 10, which
            means jack or higher)

            The appropriate payout is subsequently returned.
        """

        c = Counter(self.ids)
        m = c.most_common()[:2]
        if m[0][1] == 4:
            return 25
        elif m[0][1] == 3 and m[1][1] == 2:
            return 9
        elif m[0][1] == 3:
            return 3
        elif m[0][1] == 2 and m[1][1] == 2:
            return 2
        elif m[0][1] == 2 and m[0][0] >= 11:
            return 1
        else:
            return 0


    def check_for_flush(self):
        """
            Using the Counter object to check if all card suits in the
            hand are the same.
        """
        c = Counter(self.suits)
        m = c.most_common()[0][1]
        if m == 5:
            return 6
        else:
            return 0

    def check_for_straight(self):
        """
            In this function aces are assigned the id=1 in one instance
            and id = 14 in the next instance as aces can be counted as
            high or low in poker.

            The straight_helper is called to determine whether each card
            in the hand is one higher than the previous card
        """
        is_straight = 0

        if 14 in self.ids:
            new_ids = [i if i != 14 else 1 for i in self.ids]
            is_straight =+ self.straight_helper(self.ids)

        is_straight += self.straight_helper(self.ids)

        if is_straight:
            return 4
        else:
            return 0

    def straight_helper(self, hand_ids):
        """
            This function determine whether each card
            in the hand is one higher than the previous card
        """

        seq = sorted(hand_ids)
        it = iter(seq[1:])
        if all(int(next(it)) - int(i) == 1 for i in seq[:-1]):
            return 1
        else:
            return 0

    def check_straight_flush(self, straight, flush):
        """
            Check if hand is a straight flush and a royal flush
        """
        if flush and straight:
            if 13 in self.ids and 14 in self.ids:
                return 800
            else:
                return 50
        else:
            return 0


