import unittest
from aiController import compMove
board = [0, 1, 2, 3, 4, 5, 6, 7, 8]


class AiTest(unittest.TestCase):

    def test_check_winning_move(self):
        bcopy = board[:]
        bcopy[0] = bcopy[1] = 'C'
        self.assertEqual(compMove(bcopy), 2)

    def test_block_winning_move(self):
        bcopy = board[:]
        bcopy[3] = bcopy[4] = 'X'
        self.assertEqual(compMove(bcopy), 5)

    def test_create_double_winning(self):
        bcopy = board[:]
        bcopy[5] = bcopy[7] = 'C'
        bcopy[8] = "X"
        self.assertEqual(compMove(bcopy), 4)

    def test_block_double_winning(self):
        bcopy = board[:]
        bcopy[2] = bcopy[6] = 'X'
        bcopy[4] = "C"
        self.assertEqual(compMove(bcopy), 1)

    def test_play_middle_pos(self):
        self.assertEqual(compMove(board), 4)


if __name__ == '__main__':
    unittest.main()
