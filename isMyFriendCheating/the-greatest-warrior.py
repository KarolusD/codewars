import math


class Warrior():
    def __init__(self):
        self.level = 1
        self.experience = 100
        self.ranks = {
            0: "Pushover",
            1: "Novice",
            2: "Figter",
            3: "Warrior",
            4: "Veteran",
            5: "Sage",
            6: "Elite",
            7: "Conqueror",
            8: "Champion",
            9: "Master",
            10: "Greatest"
        }
        self.rank = self.ranks[0]
        self.achievements = []

    def gainExp(self, exp):
        prevExp = self.experience - exp
        if math.floor(self.experience/100) - math.floor(prevExp/100) >= 1 and self.level < 100:
            self.level = int(self.experience / 100)
            self.rank = self.ranks[math.floor(self.level / 10)]
            if (self.level == 100):
                self.experience = 10_000

    def training(self, lst):
        if lst[2] <= self.level:
            self.experience += lst[1]
            self.achievements.append(lst[0])
            self.gainExp(lst[1])
            return lst[0]

    # your code here
    def battle(self, enemy_lvl):
        print(self.experience, 'exp przed walka')
        if enemy_lvl <= 100 and enemy_lvl >= 1:

            if enemy_lvl == self.level:
                self.experience += 10
                self.gainExp(10)
            elif enemy_lvl == self.level - 1:
                self.experience += 5
                self.gainExp(5)
            elif enemy_lvl > self.level and enemy_lvl - self.level < 5:
                how_many_exp = 20 * \
                    (enemy_lvl-self.level)*(enemy_lvl-self.level)
                self.experience = how_many_exp
                self.gainExp(how_many_exp)

            print(self.experience, 'exp poooo walce')
            return self.battle_message(enemy_lvl)

        else:
            return "Invalid level"

    def battle_message(self, enemy_lvl):
        #print(enemy_lvl, self.level)
        if self.level >= enemy_lvl + 2:
            return 'Easy fight'
        elif self.level >= enemy_lvl + 1:
            return 'A good fight'
        elif self.level <= enemy_lvl:
            return 'An intense fight'
        elif math.floor(enemy_lvl/10) - math.floor(self.level/10) >= 1:
            return 'You\'ve been defeated'
        elif enemy_lvl - self.level >= 5:
            return 'Not strong enough'
        # However, if your warrior is at least one rank lower than your enemy,
        #  and at least 5 levels lower, your warrior cannot fight against an enemy
        #  that strong and must instead return "You've been defeated".


tom = Warrior()
#print(tom.level, 1)
#print(tom.experience, 100)
#print(tom.rank, "Pushover")

bruce_lee = Warrior()
print(bruce_lee.level, 1)
print(bruce_lee.experience, 100)
print(bruce_lee.rank, "Pushover")
print(bruce_lee.achievements, [])
print(bruce_lee.training(
    ["Defeated Chuck Norris", 9000, 1]), "Defeated Chuck Norris")
print(bruce_lee.experience, 9100)
print(bruce_lee.level, 91)
print(bruce_lee.rank, "Master")
print(bruce_lee.battle(90), "A good fight")
print(bruce_lee.experience, 9105)
print(bruce_lee.achievements, ["Defeated Chuck Norris"])
print(math.floor(895 / 100))
