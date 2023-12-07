from collections import defaultdict
from day_07 import INPUT_TEST, INPUT


class Hand:
    CARD_POINTS = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}

    def __init__(self, line):
        line = line.strip().split(' ')
        self.cards = line[0]
        self.bid = int(line[1])

        card_count = defaultdict(lambda: 0)
        for c in self.cards:
            card_count[c] += 1

        self.deck = defaultdict(str)
        for c, v in card_count.items():
            self.deck[v] += c

        major = max(self.deck.keys())

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
        else:
            self.deck_name = 'High card'
            self.major = 0

        self.minor = 0
        for icard, c in enumerate(self.cards, 1):
            self.minor += 14**-icard * Hand.CARD_POINTS[c]

        self.value = self.major + self.minor

    def __str__(self):
        return f'{self.deck_name}: {" ".join("".join(c*v) for v, c in self.deck.items())} - {self.value} - {self.bid}'

    def __lt__(self, other):
        return self.value < other.value


def day_07a(inp):
    hands = [Hand(line) for line in inp.split('\n')]
    hands.sort()

    total = 0
    for rank, hand in enumerate(hands, 1):
        print(rank, hand)
        total += rank * hand.bid

    return total


print(day_07a(INPUT_TEST))
print(day_07a(INPUT))
