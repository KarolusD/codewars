def tickets(people):
    vasya_money = {25: 0, 50: 0, 100: 0}

    for person_money in people:

        change = person_money - 25

        if change / 25 == 1:
            if vasya_money.get(25) > 0:
                vasya_money[25] -= 1
            else:
                return "NO"

        elif change / 25 == 2:
            if vasya_money.get(50) > 0:
                vasya_money[50] -= 1
            elif vasya_money.get(25) > 1:
                vasya_money[25] -= 2
            else:
                return "NO"

        elif change / 25 == 3:
            if vasya_money.get(50) > 0 and vasya_money.get(25) > 0:
                vasya_money[50] -= 1
                vasya_money[25] -= 1
            elif vasya_money.get(25) > 2:
                vasya_money[25] -= 3
            else:
                return "NO"

        vasya_money[person_money] += 1

    return "YES"


print(tickets([25, 25, 50]), "YES")
print(tickets([25, 25, 50, 50, 100]), "NO")

# 25 + 25 = 50
# 25 + 50 = 75
# 50 + 50 = 100
# 100
