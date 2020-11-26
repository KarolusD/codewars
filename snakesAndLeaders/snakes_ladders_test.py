import unittest
import snakes_ladders

game = snakes_ladders.SnakesLadders()


class TestSnakeLadders(unittest.TestCase):

    def test_01(self):
        self.assertEqual(game.play(1, 1), "Player 1 is on square 38")
        self.assertEqual(game.play(1, 5), "Player 1 is on square 44")
        self.assertEqual(game.play(6, 2), "Player 2 is on square 31")
        self.assertEqual(game.play(1, 1), "Player 1 is on square 25")


if __name__ == '__main__':
    unittest.main()
