#################################################################

#                      AUTHOR: ZEYNEP OZALP                     #

#################################################################
import copy

class Node:
    def __init__(self, tiles=[], parent=None, g=0, h=0, f=0):
        self.tiles = tiles
        self.g = g
        self.h = h
        self.f = f
        self.parent = parent
        
    def isGoal(self):
        return self.tiles == goal.tiles

    def findBlank(self): #find the blank in a node's tiles
        tiles = self.tiles
        for i in range(n):
            for j in range(n):
                if tiles[i][j] == '_':
                    return i, j

    def hgf(self): # calculate the manhattan distance
        sum = 0
        tiles = self.tiles
        if self==start:
            for i in range(n):
                for j in range(n):
                    if tiles[i][j] == '_':
                        continue
                    else:
                        x, y = findGoal(tiles[i][j])
                        sum += abs(x - i) + abs(y - j)
            self.h = sum
            self.g = 0
            self.f = sum
        else:
            for i in range(n):
                for j in range(n):
                    if tiles[i][j] == '_':
                        continue
                    else:
                        x, y = findGoal(tiles[i][j])
                        sum += abs(x - i) + abs(y - j)
            self.h = sum
            self.g = self.parent.g + 1
            self.f = self.g + sum

    def genChildren(self):
        tiles = self.tiles
        x, y = self.findBlank()
        newTiles = []
        if (x + 1) < n: #moving blank down / moving a tile up
            new = copy.deepcopy(tiles)
            new[x][y] = new[x+1][y]
            new[x+1][y] = '_'
            newTiles.append(new)
        if (x - 1) > -1: #moving blank up / moving a tile down
            new = copy.deepcopy(tiles)
            new[x][y] = new[x-1][y]
            new[x-1][y] = '_'
            newTiles.append(new)
        if (y + 1) < n:  # moving blank right / moving a tile left
            new = copy.deepcopy(tiles)
            new[x][y]=new[x][y+1]
            new[x][y+1]='_'
            newTiles.append(new)
        if (y - 1) > -1: # moving blank left / moving a tile right
            new = copy.deepcopy(tiles)
            new[x][y] = new[x][y - 1]
            new[x][y-1] = '_'
            newTiles.append(new)
        ret = []
        for i in newTiles: #create children nodes
            child = Node(i, self)
            child.hgf()
            ret.append(child)
        return ret

    def isExp(self, exp):
        tiles = self.tiles
        for i in exp:
            if (tiles == i.tiles) and (i.f<=self.f):
                return i
        return None

start = Node()
goal = Node()
m = 0
n = 0

def getInput():
    global m, n, goal, start
    m = int (input())
    n = int (input())
    tiles = []
    for i in range(n):
        tiles.append(input().split(" "))
    start.tiles = tiles
    tiles = []
    for i in range(n):
        tiles.append(input().split(" "))
    goal.tiles = tiles
    start.hgf()

def findGoal(str): #find the correct place of a tile in goal
    global goal
    tiles = goal.tiles
    for i in range(n):
        for j in range(n):
            if tiles[i][j] == str:
                return i, j

def IDAstar():
    fmax = start.f
    while(1):
        if(fmax > m):
            return None
        node, newfmax = limitedSearch(start, fmax)
        if(node!=None):
            return node
        if(newfmax!=None):
            fmax = newfmax
    return None

def limitedSearch(node, limit):
    if node.f > limit:
        return None, node.f
    if node.isGoal():
        return node, limit
    successors = node.genChildren()
    min = float('inf')
    for succ in successors:
        newNode, newLimit = limitedSearch(succ, limit)
        if newNode!=None:
            return newNode, None
        if newLimit < min:
            min = newLimit
    return None, min

def printOutput(sol):
    global goal, n
    print ("SUCCESS\n")
    path = []
    while(sol!=None):
        path.insert(0, sol)
        sol=sol.parent
    for i in range(len(path)):
        state = path[i]
        for j in range(n):
            for k in range(n):
                if(k<n-1):
                    print ((state.tiles)[j][k] + " ", end="")
                else:
                    print ((state.tiles)[j][k])
        print ("\n"),

def solve():
    global m, n, goal, start
    getInput()
    solution = None
    solution = IDAstar()

    if(solution==None):
        print ("FAILURE")
    else:
        printOutput(solution)

solve()
