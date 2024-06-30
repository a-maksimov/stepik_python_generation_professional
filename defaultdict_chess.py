from collections import defaultdict


def wins(pairs):
    wins_dict = defaultdict(set)
    for winner, loser in pairs:
        wins_dict[winner].add(loser)
    return wins_dict


result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))
