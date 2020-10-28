
from Node import Node
import copy
import random
from datetime import date, datetime


N = 5
# N = int(input("Enter the size of the game board:\n"))


def main():

    # our board is initially on a maximizing layer
    board = Node(N=N)
    board.resetGrid()

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
            board = generateComputerPlayerMove(board, depth, -1000, +1000, maximizingPlayer, 'M')[0]

            # print("printing the returned board")
            # board.draw()
            # print("________________________")
            # this returns the state to the next move we can make
            if board.parent is not None:
                while board.parent.parent:
                    # print(board.parent)
                    board = board.parent
            board.parent = None

            currentPlayer = 'H'
    
        board.draw()
        # break

        if board.checkForAWin('H' if currentPlayer == 'M' else 'M')[0]:
            print(f"{'Human' if currentPlayer == 'M' else 'Computer'} Player wins!")                        
            break


# if computer moves first computer is a maximizing player
def getWhoMovesFirst():

    maximizing = True
    first = input("Who moves first? (h/m)").upper()

    if first == 'H':
        maximizing = False
    
    return first, maximizing


def getHumanPlayerMove(board):

    invalid_move = True
    while (invalid_move):
        x = int(input('\nEnter the row of your desired move:'))
        y = int(input('\nEnter the column of your desired move:'))

        if ((x < N and y < N) and board.state[x][y] == ' '):
            board.insertMove(x, y, 'H')
            invalid_move = False
        else:
            print('\nInvalid move, please try new coordinates.')


def generateComputerPlayerMove(board, depth, alpha, beta, maximizingPlayer, playerType):

    curState = copy.deepcopy(board)
    state = None
    children = curState.generateStates(playerType)
    opponent = 'M' if (playerType == 'H') else 'H'

    # for s in children:
    #     s.draw()

    if (depth == 0 or curState.checkForAWin('M')[0] or len(children) == 0):
        return curState, staticEvaluation(curState, playerType)

    if maximizingPlayer:
        maxEvaluation = -1000
        
        # curState is the generated States
        for child in children:
            newState, evaluation = generateComputerPlayerMove(child, depth -1, alpha, beta, False, opponent)
            if evaluation > maxEvaluation:
                state = newState
            maxEvaluation = max(maxEvaluation, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        # print("maximizing")
        # state.draw()
        return state, maxEvaluation
      
    else:
        minEvaluation = 1000
        for child in children:
            newState, evaluation = generateComputerPlayerMove(child, depth - 1, alpha, beta, True, opponent)
            if evaluation < minEvaluation:
                state = newState
            minEvaluation = min(minEvaluation, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        # print("minimizing")
        # state.draw()
        return state, minEvaluation
    

def staticEvaluation(curState, playerType): #curState is a node and this assigns a value to it
    value = 0
    isWin = curState.checkForAWin(playerType)
    opponentWin = curState.checkForAWin('H' if playerType == 'M' else 'M')

    #Find all possible winning paths from the current state.

    #mini_lists = [x,y,0]
    ex_1 = [1,4,0]
    ex_2 = [3,7,0]
    ex_3 = [2,1,0]
    ex_4 = [3,8,0]

    #possiblepath
    path1 = [ex_1,ex_2,ex_3,ex_4]

    #mini_lists = [x,y,0]
    ex_1 = [1,4,0]
    ex_2 = [8,1,0]
    ex_3 = [2,1,0]
    ex_4 = [6,6,0]

    #possiblepath
    path2 = [ex_1,ex_2,ex_3,ex_4]

    #mini_lists = [x,y,0]
    ex_1 = [1,4,0]
    ex_2 = [7,7,0]
    ex_3 = [8,2,0]
    ex_4 = [2,6,0]

    #possiblepath
    path3 = [ex_1,ex_2,ex_3,ex_4]

    possiblePaths =[path1, path2, path3]

    #---------> make the vertices have a 3rd blank index


    #Log all vertices that are in a winning path

    verticesInPaths = []

    for path in possiblePaths:
        for vertex in path:
            if curState.state[vertex[0]][vertex[1]] != 'M':
                verticesInPaths.append(vertex)

    #Count the number of winning paths that go through each vertex.

    for vertex in verticesInPaths:
        vertex[2] = verticesInPaths.count(vertex)

    #Sort the selected vertices list based on how many paths they're in.

    sorted(verticesInPaths, key = lambda x: x[2])
    winningVertex = verticesInPaths[0]

    #(Can range from once up to the number of possible winning paths found.)

    #All vertices on the grid that are in the above group, means that they are not 
    #in the path of a winning option, and are given a low value. (Or none?)
    #Maybe doesn't even matter since the other ones will be chosen anyways.

    #Select the vertex with the highest number.
    print('Based on this method alone, the next best move is the vertex ({:d},{:d}) as it is a vertex in {:d} possible winning paths.'.format(winningVertex[0], winningVertex[1], winningVertex[2]))

    
    
    
    
    
    
    return value
    
    #-------------------
    
    # if this is a winning state give it a high value
    if isWin[0]:
        value += 100
    # if this is a losing state give it a low value
    if opponentWin[0]:
        value -= 100
    
    
    # depending on path length add a value

    # depending on opponents path length subtract a value

    # if we place it in a column with no playerType give add to value else + 0?

    # random.seed(datetime.now())
    # curState.heuristic = random.randint(1, 50)
    # # print(f"heuristic value = {curState.heuristic}")
    # return curState.heuristic

    # if all up, down, left, right is other player or out of bounds

    return value


if __name__ == "__main__":
    main()
