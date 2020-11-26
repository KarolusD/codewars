class SnakesLadders():
    def __init__(self):
        # 2, 7, 8,15,16,21,28,36,46,49,51,62,64,71,74,78,87,89,92,95,99
        self.board = {
            2: 38,
            7: 14,
            8: 31,
            15: 26,
            16: 6,
            21: 42,
            28: 84,
            36: 44,
            46: 25,
            49: 11,
            51: 67,
            62: 19,
            64: 60,
            71: 91,
            74: 53,
            78: 98,
            87: 94,
            89: 68,
            92: 88,
            95: 75,
            99: 80
        }
        self.player1 = 0
        self.player2 = 0
        self.first_player_move = True
        self.win = False

    def final_position(self, pos):
        return self.board.get(pos, pos)

    def who_will_move(self, die1, die2):
        return self.first_player_move if (die1 == die2) else not self.first_player_move

    def play(self, die1, die2):
        if (self.win):
            return 'Game over!'

        die_sum = die1 + die2
        pos = 0
        player_name = ''

        if (self.first_player_move):
            pos = self.player1
            player_name = 'Player 1'
        else:
            pos = self.player2
            player_name = 'Player 2'

        if (pos + die_sum == 100):
            self.win = True
            return f'{player_name} Wins!'
        elif (pos + die_sum > 100):
            pos = 200 - pos - die_sum
        else:
            pos += die_sum

        pos = self.final_position(pos)

        if (self.first_player_move):
            self.player1 = pos
        else:
            self.player2 = pos

        message = f'{player_name} is on square {pos}'
        self.first_player_move = self.who_will_move(die1, die2)
        return message


r = [(5, 3), (4, 6), (1, 2), (4, 4), (4, 3), (2, 6),
     (5, 1), (5, 6), (6, 5), (1, 2), (2, 4), (4, 2)]

game = SnakesLadders()

for (die1, die2) in r:
    print(f'{game.play(die1, die2)} | {game.first_player_move}')
