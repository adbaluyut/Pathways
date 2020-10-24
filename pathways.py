
from Node import Node
import copy
import queue

N = 5
# N = int(input("Enter the size of the game board:\n"))


def main():

    board = Node(N=N)
    board.resetGrid()
    board.insertMove(2, 0, 'H')
    board.insertMove(2, 2, 'H')
    board.insertMove(3, 3, 'H')
    board.insertMove(4, 4, 'H')
    board.insertMove(0, 4, 'H')
    # board.draw()
    # getHumanPlayerMove(board)
    # board.draw()
    # board.generateStates()
    board.draw()
    if (board.checkForAWin('H')):
        print('Win!')
    else:
        print('nah brah')


def getWhoMovesFirst():

    return input("Who moves first? (h/m)")


def getHumanPlayerMove(board):
    invalid_move = True
    while (invalid_move):
        x = int(input('\nEnter the x coordinate of your desired move:'))
        y = int(input('\nEnter the y coordinate of your desired move:'))

        if ((x < N and y < N) and board.state[x][y] == ' '):
            board.insertMove(x, y, 'H')
            invalid_move = False
        else:
            print('\nInvalid move, please try new coordinates.')


def generateComputerPlayerMove():
    pass


# def checkForAWin(board, playerType):
#     nums = queue.Queue()
#     nums.put("")
#     add = ""

#     while not findEnd(board, add, playerType): 
#         add = nums.get()
#         #print(add)
#         for j in ["L", "R", "U", "D"]:
#             put = add + j
#             if valid(board, put, playerType):
#                 nums.put(put)


# def valid(board, moves, playerType):
#     # for x, pos in enumerate(board[0]):
#     #     if pos == "O":
#     #         start = x

#     i = start
#     j = 0
#     for move in moves:
#         if move == "L":
#             i -= 1

#         elif move == "R":
#             i += 1

#         elif move == "U":
#             j -= 1

#         elif move == "D":
#             j += 1

#         if not(0 <= i < len(board[0]) and 0 <= j < len(board)):
#             return False
#         elif (board[j][i] == " " or board[j][i] != playerType):
#             return False

#     return True


# def findEnd(board, moves, playerType):
#     i, j = 0, 0
#     iDest, jDest = 0, 0
#     for s in range(N):
#         if board[s][0] == playerType:
#             i = s
#             j = 0
#         for d in range(N):
#             if board[d][N - 1] == playerType:
#                 iDest = d
#                 jDest = N - 1

#     for move in moves:
#         if move == "L":
#             i -= 1

#         elif move == "R":
#             i += 1

#         elif move == "U":
#             j -= 1

#         elif move == "D":
#             j += 1

#     if board[j][i] == playerType and (i, j) == (iDest, jDest):
#         print("Found: " + moves)
#         # printMaze(board, moves)
#         return True

#     return False

def minimax(board):
    b = copy.deepcopy(board)


def alpha_beta(board):
    b = copy.deepcopy(board)


if __name__ == "__main__":
    main()
