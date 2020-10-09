
class Node:

    def __init__(self, state=None, rows=None, cols=None, parent=None):
        self.state = state
        self.rows = rows
        self.cols = cols
        self.parent = parent


    def resetGrid(self):

        self.state = []

        for i in range(self.rows): 
            self.state.append([])
            for j in range(self.cols):
                
                if (i % 2) == 0 and (j % 2) == 1:
                    self.state[i].append('H')
                elif (i % 2) == 1 and (j % 2) == 0:
                    self.state[i].append('M')
                else:
                    self.state[i].append(' ')

    
    def draw(self):
        for i in range(self.rows):
            for j in range(self.cols):
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

    
    def checkPaths(self):
        pass


    def pathUp(self):
        pass


    def checkForAWin(self,r,c,playerType):
        leftValid = False
        rightValid = False
        
        # move left
        if c > 0:
            if self.state[r][c-1] == playerType:
                pass

        # move up
        if r > 0:
            if self.state[r-1][c] == playerType:
                pass
            
        # move down

        # move right

        return leftValid and rightValid

