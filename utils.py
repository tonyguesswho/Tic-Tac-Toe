import random


def display_board(board):
    print(
        f'''
        {board[0]} | {board[1]} | {board[2]}
        ---------
        {board[3]} | {board[4]} | {board[5]}
        ---------
        {board[6]} | {board[7]} | {board[8]}
        ---------
        '''
    )


def checkMarch(board, letter, pos1, pos2, pos3):
    if board[pos1] == letter and board[pos2] == letter and board[pos3] == letter:
        return True


def checkOutcome(board, char):
    if checkMarch(board, char, 0, 1, 2):
        return True
    if checkMarch(board, char, 3, 4, 5):
        return True
    if checkMarch(board, char, 6, 7, 8):
        return True
    if checkMarch(board, char, 0, 3, 6):
        return True
    if checkMarch(board, char, 1, 4, 7):
        return True
    if checkMarch(board, char, 2, 5, 8):
        return True
    if checkMarch(board, char, 0, 4, 8):
        return True
    if checkMarch(board, char, 2, 4, 6):
        return True


def testWinMove(b, mark, i):
    bCopy = b[:]
    bCopy[i] = mark
    return checkOutcome(bCopy, mark)


def testPseudoCheckmate(b, mark, i):
    # Determines if a move opens up a fork
    bCopy = b[:]
    bCopy[i] = mark
    winningMoves = 0
    for j in range(0, 9):
        if testWinMove(bCopy, mark, j) and isinstance(bCopy[j], int):
            winningMoves += 1
    if(winningMoves >= 2):
        return winningMoves >= 2


def selectRandom(li):
    limit = len(li)
    r = random.randrange(0, limit)
    return li[r]


def fullBoard(board):
    board_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    available = board[:]
    for index, item in enumerate(board):
        if item in board_indexes:
            available[index] = True
        else:
            available[index] = False
    if any(available):
        return False
    else:
        return True


def spaceIsFree(board, pos):
    return isinstance(board[pos], int)


def insertLetter(board, letter, pos):
    board[pos] = letter
    return board
