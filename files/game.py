import unittest
from model import *

class TestGameLogic(unittest.TestCase):

    def test_first(self):
        board_solution_1 = ((1, 2, 3, 4, 5, 6, 7, 8, 9),15), ((6,7,8,9,11,12,13,15,17),36), ((2,10,15,18,23,28,31,36,44),69)
        random.choice((((1, 2, 3, 4, 5, 6, 7, 8, 9), 15),((6,7,8,9,11,12,13,15,17),36),((2,10,15,18,23,28,31,36,44),69)))
        
        new_board = Board(board_solution_1, 15)
        new_game = Game(new_board)
        new_game.start()
        new_game.player1.select_square(3)
        new_game.next_turn()
        self.assertEqual(new_game.game_finished(), False) 
        new_game.player2.select_square(5)
        new_game.next_turn()
        new_game.player1.select_square(8)
        new_game.next_turn()
        new_game.player2.select_square(9)
        new_game.next_turn()
        self.assertEqual(new_game.game_finished(), False)
        new_game.player1.select_square(4)
        self.assertEqual(new_game.game_finished(), (True, new_game.player1))
        print("testing")


   

if __name__ == '__main__':
    unittest.main()