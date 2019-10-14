from utils import display_board, fullBoard, checkOutcome, insertLetter
from aiController import compMove
from playerController import playerMove


def main():
    print('Welcome to Tic Tac Toe!')
    display_board(board)

    while not(fullBoard(board)):
        if not(checkOutcome(board, 'C')):
            newBoard = playerMove(board)
            display_board(newBoard)
        else:
            print('The Computer won')
            break

        if not(checkOutcome(board, 'X')):
            move = compMove(board)
            if move == -1:
                print('Tie Game!')
                return
            else:
                newBoard = insertLetter(board, 'C', move)
                print('Computer placed a \'C\' in position', move, ':')
                display_board(newBoard)
        else:
            print('You won this time! Good Job!')
            break

    if fullBoard(board):
        print('Tie Game!')


while True:
    start = input('Are you ready to start? (Y/N)')
    if start.lower() == 'y' or start.lower == 'yes':
        board = [x for x in range(0, 9)]
        print('###################################')
        main()
    else:
        break
