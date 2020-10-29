
from Node import Node
import copy
import random
from datetime import date, datetime


while True:
    N = input("Enter the size(N) of the game board (N x N):\n")
    if N.isdigit():
        N = int(N)
    if type(N) is int and N > 4:
        break
    print("Choose a valid int greater than 4.")


def main():

    board = Node(N=N)
    board.resetGrid()

    test = createEvalTable(board.state)
    # for i in test:
    #     print(i)

    playGame(board)


def playGame(board):
    
    board.draw()

    depth = 3
    currentPlayer, maximizingPlayer = getWhoMovesFirst()

    while True:

        if board.isFull():
            print("It's a draw!")
            break

        if currentPlayer == 'H':

            getHumanPlayerMove(board)
            currentPlayer = 'M'
        
        else:

            print("Computer making it's move")
            temp = generateComputerPlayerMove(board, board, depth, -1000, +1000, maximizingPlayer, 'M')[0]
            if temp is not None:
                board = temp
            
            if board.parent is not None:
                while board.parent.parent:
                    # print(board.parent)
                    board = board.parent
            board.parent = None

            currentPlayer = 'H'
    
        board.draw()

        if board.checkForAWin('H' if currentPlayer == 'M' else 'M')[0]:
            print(f"{'Human' if currentPlayer == 'M' else 'Computer'} wins!")                        
            break


def getWhoMovesFirst():

    maximizing = True
    while True: 
        first = input("Who moves first? (h/m)").upper()
        if first == 'H' or first == 'M':
            break
    
    return first, maximizing


def getHumanPlayerMove(board):

    invalid_move = True
    while (invalid_move):

        while True:
            x = input('\nEnter the row of your desired move:')
            if x.isdigit():
                x = int(x)
            if type(x) is int:
                break
        while True:
            y = input('\nEnter the column of your desired move:')
            if y.isdigit():
                y = int(y)
            if type(y) is int:
                break

        if ((x < N and y < N) and board.state[x][y] == ' '):
            board.insertMove(x, y, 'H')
            invalid_move = False
        else:
            print('\nInvalid move, please try new coordinates.')


def generateComputerPlayerMove(board, staticBoard, depth, alpha, beta, maximizingPlayer, playerType):

    curState = copy.deepcopy(board)
    state = None
    children = curState.generateStates(playerType)
    opponent = 'M' if (playerType == 'H') else 'H'

    if (depth == 0 or curState.checkForAWin('M')[0] or len(children) == 0):
        if curState is None:
            return
        return curState, staticEvaluation(curState, staticBoard, playerType)

    if maximizingPlayer:
        maxEvaluation = -100000
        
        # curState is the generated States
        for child in children:
            newState, evaluation = generateComputerPlayerMove(child, staticBoard, depth -1, alpha, beta, False, opponent)
            if evaluation > maxEvaluation:
                state = newState
            maxEvaluation = max(maxEvaluation, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return state, maxEvaluation
      
    else:
        minEvaluation = 100000
        for child in children:
            newState, evaluation = generateComputerPlayerMove(child, staticBoard, depth - 1, alpha, beta, True, opponent)
            if evaluation < minEvaluation:
                state = newState
            minEvaluation = min(minEvaluation, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return state, minEvaluation
    

def staticEvaluation(curState, staticBoard, playerType):
    
    value = 0
    table = createEvalTable(staticBoard.state)
    isWin = curState.checkForAWin(playerType)
    opponentWin = curState.checkForAWin('H' if playerType == 'M' else 'M')

    for i in range(N):
        for j in range(N):
            if curState.state[i][j] != staticBoard.state[i][j]:
                value += table[i][j]
    
    # if this is a winning state give it a high value
    if isWin[0]:
        value += 100
    # if this is a losing state give it a low value
    if opponentWin[0]:
        value -= 200

    return value

# def createEvalTable(board):
    
#     b = copy.deepcopy(board)
#     topoMap = copy.deepcopy(board)

#     maxValue = 1000
#     minValue = -1000
#     lt_score = 200
#     gt_score = 200

#     for i in range(N):
#         for j in range(N): 

#             if j == (N - 1) // 2:
#                 topoMap[i][j] = maxValue - 150
            
#             # center values
#             if i == (N - 1) // 2 and j == (N - 1) // 2:
#                 topoMap[i][j] = maxValue

#             # if column is less than half
#             if  j < (N - 1) // 2:
#                 topoMap[i][j] = minValue + lt_score
#                 lt_score = lt_score + 200

#             # if column is greater than half
#             if j > (N - 1) // 2:
#                 topoMap[i][j] = maxValue - gt_score
#                 gt_score = gt_score + 200

#             if i == 0:
#                 topoMap[i][j] = minValue
#             elif i == N - 1:
#                 topoMap[i][j] = minValue
#             if j == 0:
#                 topoMap[i][j] = minValue
#             elif j == N - 1:
#                 if N % 2 == 1:
#                     topoMap[i][j] = minValue
#                 else:
#                     topoMap[i][j] = maxValue - 100
    
#     # for i in topoMap:
#     #     print(i)
    
#     for i in range(N):
#         for j in range(N):
#             if board[i][j] == ' ':
#                 b[i][j] = topoMap[i][j]
#     # for i in b:
#     #     print(i)
                
#     return b

def createEvalTable(board):
    
    b = copy.deepcopy(board)
    maxValue = 1000
    minValue = -1000
    count = 0

    
    for i in range(N):
        for j in range(N):
            if board[i][j] == ' ':

                b[i][j] = 500

                if i == 0:
                    b[i][j] = minValue
                elif i == N - 1:
                    b[i][j] = minValue
                if j == 0:
                    b[i][j] = minValue
                elif j == N - 1:
                    b[i][j] = minValue               
                # if the board is in the middle
                if i == (N - 1) // 2 and j == (N - 1) // 2:
                    b[i][j] = maxValue

    return b


if __name__ == "__main__":
    main()
