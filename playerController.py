from utils import spaceIsFree, insertLetter


def playerMove(board):
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (0-8): ')
        try:
            move = int(move)
            if move >= 0 and move < 9:
                if spaceIsFree(board, move):
                    run = False
                    board = insertLetter(board, 'X', move)
                    return board
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
