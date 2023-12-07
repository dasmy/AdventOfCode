from collections import defaultdict
from day_07 import INPUT_TEST, INPUT, INPUT_TEST_2


class Hand:
    CARD_POINTS = {'A': 13, 'K': 12, 'Q': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}

    def __init__(self, line):
        line = line.strip().split(' ')
        self.cards = line[0]
        self.bid = int(line[1])

        card_count = defaultdict(lambda: 0)
        for c in self.cards:
            card_count[c] += 1

        num_jokers = card_count['J']
        del card_count['J']

        self.deck = defaultdict(str)
        for c, v in card_count.items():
            self.deck[v] += c

        if self.deck:
            major = max(self.deck.keys())

            if num_jokers:
                major_cards = self.deck[major]
                new_major = major + num_jokers
                self.deck[new_major] = major_cards[0]
                if len(major_cards) > 1:
                    self.deck[major] = major_cards[1:]
                else:
                    del self.deck[major]

                major = new_major
        else:
            major = 5  # 5 jokers

        if major == 5:
            self.deck_name = 'Five of a kind'
            self.major = 6
        elif major == 4:
            self.deck_name = 'Four of a kind'
            self.major = 5
        elif major == 3:
            if 2 in self.deck:
                self.deck_name = 'Full house'
                self.major = 4
            else:
                self.deck_name = 'Three of a kind'
                self.major = 3
        elif major == 2:
            if len(self.deck[2]) >= 2:
                self.deck_name = 'Two pairs'
                self.major = 2
            else:
                self.deck_name = 'One pair'
                self.major = 1
        elif major == 1:
            self.deck_name = 'High card'
            self.major = 0
        else:
            assert False

        if num_jokers:
            self.deck[num_jokers] += 'J'

        self.minor = 0
        for icard, c in enumerate(self.cards, 1):
            self.minor += 14**-icard * Hand.CARD_POINTS[c]

        self.value = self.major + self.minor

    def __str__(self):
        return f'{self.deck_name}: {self.cards} - {" ".join("".join(c*v) for v, c in self.deck.items())} - {self.value} - {self.bid}'

    def __lt__(self, other):
        return self.value < other.value


def day_07b(inp):
    hands = [Hand(line) for line in inp.split('\n')]
    hands.sort()

    total = 0
    for rank, hand in enumerate(hands, 1):
        print(rank, hand)
        total += rank * hand.bid

    return total


print(day_07b(INPUT_TEST))
print(day_07b(INPUT_TEST_2))
print(day_07b(INPUT))
