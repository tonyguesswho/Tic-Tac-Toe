import random
board_range = range(0, 9)
board = [x for x in board_range]


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


def spaceIsFree(pos):
    return isinstance(board[pos], int)


def insertLetter(letter, pos):
    board[pos] = letter


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


def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (0-8): ')
        try:
            move = int(move)
            if move >= 0 and move < 9:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def compMove():
    possibleMoves = [x for x, letter in enumerate(
        board) if isinstance(letter, int)]
    move = -1

    for mv in ['C', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = mv
            if checkOutcome(boardCopy, mv):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [0, 2, 6, 8]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 4 in possibleMoves:
        move = 4
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [1, 3, 5, 7]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


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


def main():
    print('Welcome to Tic Tac Toe!')
    display_board(board)

    while not(fullBoard(board)):
        if not(checkOutcome(board, 'C')):
            playerMove()
            display_board(board)
        else:
            print('The Computer won')
            break

        if not(checkOutcome(board, 'X')):
            move = compMove()
            if move == -1:
                print('Tie Game!')
                return
            else:
                insertLetter('C', move)
                print('Computer placed a \'C\' in position', move, ':')
                display_board(board)
        else:
            print('You won this time! Good Job!')
            break

    if fullBoard(board):
        print('Tie Game!')


while True:
    start = input('Are you ready to start? (Y/N)')
    if start.lower() == 'y' or start.lower == 'yes':
        board = [x for x in board_range]
        print('###################################')
        main()
    else:
        break
