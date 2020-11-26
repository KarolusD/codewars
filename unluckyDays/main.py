import datetime


def unlucky_days(year):
    black_fridays = 0
    for i in range(1, 13):
        d = datetime.date(year, i, 13)
        if (d.weekday() == 4):
            black_fridays += 1

    return black_fridays


print(unlucky_days(2015), 3)
print(unlucky_days(1986), 1)
