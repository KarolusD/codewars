class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, activity_rank):

        if activity_rank < -8 or activity_rank > 8 or activity_rank == 0:
            raise ValueError()
        print(self.rank, '--> rank')
        print(self.progress, '--> progress')
        print(activity_rank, '--> activity_rank')
        if (self.rank == 8):
            return
        if self.rank == activity_rank:
            self.progress += 3
        elif self.rank == activity_rank + 1 \
                or (self.rank == 1 and activity_rank == -1):
            self.progress += 1
        elif self.rank < activity_rank:
            if self.rank < 0 and activity_rank > 0:
                d = activity_rank - self.rank - 1
            else:
                d = activity_rank - self.rank
            self.progress += 10 * d * d

        if self.progress >= 100:
            if self.rank + self.progress//100 >= 0 and self.rank < 0:
                self.rank += self.progress//100 + 1
            else:
                self.rank += self.progress//100
            if self.rank == 0:
                self.rank = 1
            elif self.rank >= 8:
                self.rank = 8
                self.progress = 0

            self.progress = self.progress % 100


user = User()
user.rank = 1
user.progress = 61
user.inc_progress(8)
print(user.rank, 6)
print(user.print)

# 1 --> rank
# 61 --> progress
# 8 --> activity_rank
'''
After applying rank of 8 the resulting 
user rank was expected to be 6, but was actually 7:
7 should equal 6
'''