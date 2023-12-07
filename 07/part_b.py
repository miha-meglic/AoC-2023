import aocd
from collections import Counter

order = 'AKQT98765432J'
sorter = lambda tup: [order.index(c) for c in tup[0]]

data = aocd.get_data(day=7, year=2023)

five = []
four = []
house = []
three =[]
two_two = []
two = []
high = []

for turn in data.splitlines():
    [hand, bet] = turn.split(' ')
    cnt = Counter(hand)

    vals = cnt.values()
    if 5 in vals:
        five.append((hand, bet))
    elif 4 in vals:
        if cnt['J']:
            five.append((hand, bet))
        else:
            four.append((hand, bet))
    elif 3 in vals and 2 in vals:
        if cnt['J']:
            five.append((hand, bet))
        else:
            house.append((hand, bet))
    elif 3 in vals:
        if cnt['J'] and cnt['J'] == 2 or cnt['J'] and cnt['J'] == 3 and 2 in vals:
            # JJJXX or XXXJJ
            five.append((hand, bet))
        elif cnt['J'] and (cnt['J'] == 1 or cnt['J'] == 3):
            # JJJXY or XXXJY
            four.append((hand, bet))
        else:
            three.append((hand, bet))
    elif 2 in vals:
        if 2 in Counter(vals).values():
            if cnt['J'] and cnt['J'] == 2:
                four.append((hand, bet))
            elif cnt['J'] and cnt['J'] == 1:
                house.append((hand, bet))
            else:
                two_two.append((hand, bet))
        else:
            if cnt['J']:
                three.append((hand, bet))
            else:
                two.append((hand, bet))
    else:
        if cnt['J']:
            two.append((hand, bet))
        else:
            high.append((hand, bet))

ordered = sorted(five, key=sorter) + sorted(four, key=sorter) + sorted(house, key=sorter) + sorted(three, key=sorter) + sorted(two_two, key=sorter) + sorted(two, key=sorter) + sorted(high, key=sorter)

total = 0
for i, (_, bet) in enumerate(ordered[::-1]):
    total += (i + 1) * int(bet)

print(total)
