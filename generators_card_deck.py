def card_deck(suit):
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    suits = ["пик", "треф", "бубен", "червей"]
    suits.remove(suit)
    index = 0
    card = f'{values[index]} {suits[index]}'
    while True:
        yield card
        index += 1
        card = f'{values[index % len(values)]} {suits[(index // len(values)) % len(suits)]}'


generator = card_deck('пик')

print(next(generator))
print(next(generator))
print(next(generator))

print()

generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]

print(*cards)