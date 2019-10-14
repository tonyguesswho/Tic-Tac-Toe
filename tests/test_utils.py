import unittest
from utils import checkMarch, checkOutcome,\
     testWinMove, fullBoard, spaceIsFree, insertLetter
board = [0, 1, 2, 'X', 'X', 'X', 6, 7, 8]


class UtilTest(unittest.TestCase):

    def test_check_march(self):
        self.assertEqual(checkMarch(board, 'X', 3, 4, 5), True)

    def test_check_outcome(self):
        self.assertEqual(checkOutcome(board, 'X'), True)

    def test_winning_move_false(self):
        self.assertEqual(testWinMove(board, 'C', 8), None)

    def test_winning_move_true(self):
        self.assertEqual(testWinMove(board, 'X', 8), True)

    def test_fullboard_true(self):
        self.assertEqual(fullBoard(['X', 'C', 'X']), True)

    def test_fullboard_false(self):
        self.assertEqual(fullBoard(board), False)

    def test_spacefree_true(self):
        self.assertEqual(spaceIsFree(board, 2), True)

    def test_spacefree_false(self):
        self.assertEqual(spaceIsFree(board, 4), False)

    def test_insert_letteer(self):
        bcopy = board[:]
        bcopy[1] = 'X'
        self.assertEqual(insertLetter(board, 'X', 1), bcopy)


if __name__ == '__main__':
    unittest.main()
