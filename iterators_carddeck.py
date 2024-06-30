class CardDeck:
    def __init__(self):
        self.m = ("пик", "треф", "бубен", "червей")
        self.values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.m) * len(self.values):
            raise StopIteration
        return f'{self.values[self.index % 13]} {self.m[(self.index // 13) % 4]}'


cards = list(CardDeck())

print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])