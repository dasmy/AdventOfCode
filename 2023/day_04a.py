from day_04 import INPUT_TEST, INPUT


def day_04a(inp):
    total = 0
    for game in inp.split('\n'):
        decks = game.split(': ')[1]

        cards = []
        for deck in decks.split(' | '):
            cards.append(set(filter(None, deck.split(' '))))

        winning_numbers = cards[0].intersection(cards[1])

        if winning_numbers:
            points = 2**(len(winning_numbers)-1)
            total += points

    return total


print(day_04a(INPUT_TEST))
print(day_04a(INPUT))
