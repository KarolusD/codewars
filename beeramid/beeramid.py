import math


def beeramid(bonus, price):
    # your code
    # 1, 4, 9, 16, 25,
    # 1+3 = 4
    # 4+5 = 9
    # 9+7 = 16
    # 16+9 = 25
    beers_you_can_buy = math.floor(bonus/price)
    if beers_you_can_buy < 1:
        return 0
    elif beers_you_can_buy < 5:
        return 1

    # you can buy 5 beers
    beers = 1
    level = 0
    counter = 3
    all_beers = 0

    while True:
        if (all_beers >= beers_you_can_buy):
            break
        print(beers)
        beers += counter
        all_beers += beers
        counter += 2
        level += 1

    return level


#print(beeramid(9, 2),  1)
#print(beeramid(21, 1.5),  3)
#print(beeramid(-1, 4), 0)
print(beeramid(455, 5), 6)
