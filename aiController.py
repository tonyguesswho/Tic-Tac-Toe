from utils import selectRandom, checkOutcome, testPseudoCheckmate


def compMove(board):
    possibleMoves = [x for x, letter in enumerate(
        board) if isinstance(letter, int)]
    move = -1

    for mv in ['C', 'X']:  # check for winning move or block player winning move
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = mv
            if checkOutcome(boardCopy, mv):
                move = i
                return move

    for i in possibleMoves:  # check for double winning opportunity
        if testPseudoCheckmate(board, 'C', i):
            return i

    playerOp = 0
    for i in possibleMoves:  # check for players double winning opportunity
        if testPseudoCheckmate(board, 'X', i):
            playerOp += 1
            tempMove = i
    if playerOp == 1:
        return tempMove
    elif playerOp == 2:
        for j in [1, 3, 5, 7]:
            if isinstance(board[j], int):
                return j

    if 4 in possibleMoves:  # attack middle space
        move = 4
        return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [0, 2, 6, 8]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:  # pick random corner
        move = selectRandom(cornersOpen)
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [1, 3, 5, 7]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:  # pick random corner
        move = selectRandom(edgesOpen)

    return move
