from day_04 import INPUT_TEST, INPUT


def day_04b(inp):
    card_counts = dict((igame, 1) for igame in range(len(inp.split('\n'))))

    for igame, game in enumerate(inp.split('\n')):
        decks = game.split(': ')[1]

        cards = []
        for deck in decks.split(' | '):
            cards.append(set(filter(None, deck.split(' '))))

        winning_numbers = cards[0].intersection(cards[1])
        win_count = len(winning_numbers)

        if win_count:
            for iskip in range(win_count):
                card_copy = igame + iskip + 1
                if card_copy in card_counts:
                    card_counts[card_copy] += card_counts[igame]

            print(igame+1, win_count, list(card_counts.values()))

    return sum(c for c in card_counts.values())


print(day_04b(INPUT_TEST))
print(day_04b(INPUT))
