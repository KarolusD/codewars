# https://www.codewars.com/kata/6089c7992df556001253ba7d/train/python
class Song:
    def __init__(self, title: str, artist: str = 'unknown'):
        self.title = title
        self.artist = artist
        self.users = set()

    def how_many(self, users):
        # checking current set length
        # adding users to set
        # checking set length after adding users
        # comparing previous and current set length
        # returning the length difference
        count = len(self.users)
        self.users.update(list(map(lambda x: x.lower(), users)))
        return len(self.users)-count

    # def toLowerCase(user):
    #   return user.lower()


mount_moose = Song('Beat it')
print(f'title: {mount_moose.title},  author: {mount_moose.artist}')

u1 = mount_moose.how_many(['John', 'Fred', 'BOb', 'carl', 'RyAn'])
u2 = mount_moose.how_many(['John', 'Dave', 'BOb', 'carl', 'RyAn'])
print(u1, u2)
