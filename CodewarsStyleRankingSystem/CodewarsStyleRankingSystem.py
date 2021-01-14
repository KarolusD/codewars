class User:
    pass


user = User()
print(user.rank, -8)
print(user.progress, 0)
user.inc_progress(-7)
print(user.progress, 10)
user.inc_progress(-5)
print(user.progress, 0)
print(user.rank, -7)
