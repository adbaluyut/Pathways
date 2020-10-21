
import copy

class Node:

    def __init__(self, state=None, N=None, parent=None):
        self.state = state
        self.N = N
        self.parent = parent


    def resetGrid(self):

        self.state = []

        for i in range(self.N): 
            self.state.append([])
            for j in range(self.N):
                
                if (i % 2) == 0 and (j % 2) == 1:
                    self.state[i].append('H')
                elif (i % 2) == 1 and (j % 2) == 0:
                    self.state[i].append('M')
                else:
                    self.state[i].append(' ')

    
    def draw(self):
        for i in range(self.N - 1, -1, -1):
            for j in range(self.N):
                print(f'{self.state[i][j]}', end=' ')
            print()        
        print()


    def insertMove(self, r, c, playerType):
        self.state[r][c] = playerType


    def up(self, index):
        pass


    def down(self, index):
        pass


    def left(self, index):
        pass


    def right(self, index):
        pass


    def checkMoves(self):
        index = self.findEmpty()
        neighbors = []
        neighbors.append(self.up(index))
        neighbors.append(self.down(index))
        neighbors.append(self.left(index))
        neighbors.append(self.right(index))
        
        return [i for i in neighbors if i]


    def generateStates(self):
        stateList = []

        for i in range(self.N):
            for j in range(self.N):
                if self.state[i][j] == ' ':
                    self.state[i][j] ='M'
                    self.state[i][j] = ' '
                    # New Node will have a copy of board.state
                    stateOption = Node(N=self.N, state=copy.deepcopy(self.state), parent=self)
                    # New Node.state[i][j] = 'M'
                    stateOption.state[i][j] = 'M'
                    # store the state
                    stateList.append(stateOption)
        
        for state in stateList:
            state.draw()
            
        print(len(stateList))
                    

    def checkForAWin(self,r,c,playerType):

        for i in range(self.N):
            for j in range(self.N):
                if self.state[i][j] == playerType:
                    startingState = self.state[i][j]
                    break

        
        pass

