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

    def findBlank(self):  # find the blank in a node's tiles
        tiles = self.tiles
        for i in range(n):
            for j in range(n):
                if tiles[i][j] == '0':
                    return i, j


    def calculate_fgh2(self):  # calculate f(n), g(n), and h(n) using h2: euclidean distance
        sum = 0
        tiles = self.tiles
        if self == start:
            for i in range(n):
                for j in range(n):
                    if tiles[i][j] == '0':
                        continue
                    else:
                        x, y = findGoal(tiles[i][j])
                        sum += round(((i - x)**2 + (j - y)**2)**(1/2))
            self.h = sum
            self.g = 0
            self.f = sum
        else:
            for i in range(n):
                for j in range(n):
                    if tiles[i][j] == '0':
                        continue
                    else:
                        x, y = findGoal(tiles[i][j])
                        sum += round(((i - x)**2 + (j - y)**2)**(1/2))
            self.h = sum
            self.g = self.parent.g + 1
            self.f = self.g + sum

    def genChildren(self):
        tiles = self.tiles
        x, y = self.findBlank()
        newTiles = []
        if (x + 1) < n:  # moving blank down / moving a tile up
            new = copy.deepcopy(tiles)
            new[x][y] = new[x+1][y]
            new[x+1][y] = '0'
            newTiles.append(new)
        if (x - 1) > -1:  # moving blank up / moving a tile down
            new = copy.deepcopy(tiles)
            new[x][y] = new[x-1][y]
            new[x-1][y] = '0'
            newTiles.append(new)
        if (y + 1) < n:  # moving blank right / moving a tile left
            new = copy.deepcopy(tiles)
            new[x][y] = new[x][y+1]
            new[x][y+1] = '0'
            newTiles.append(new)
        if (y - 1) > -1:  # moving blank left / moving a tile right
            new = copy.deepcopy(tiles)
            new[x][y] = new[x][y - 1]
            new[x][y-1] = '0'
            newTiles.append(new)
        ret = []
        for i in newTiles:  # create children nodes
            child = Node(i, self)
            child.calculate_fgh2()
            ret.append(child)
        return ret


start = Node()
goal = Node()
depth = 0
n = 0


def getInput():
    global depth, n, goal, start
    depth = 1000
    n = 3
    tiles = []
    print("INITIAL state input: ")
    for i in range(n):
        tiles.append(input().split(" "))
    start.tiles = tiles
    tiles = []
    print("\nGOAL state input: ")
    for i in range(n):
        tiles.append(input().split(" "))
    goal.tiles = tiles
    print()
    start.calculate_fgh2()


def findGoal(str):  # find the correct place of a tile in goal
    global goal
    tiles = goal.tiles
    for i in range(n):
        for j in range(n):
            if tiles[i][j] == str:
                return i, j


def IDAstar():
    fmax = start.f
    while(1):
        if(fmax > depth):
            return None
        node, newfmax = limitedSearch(start, fmax)
        if(node != None):
            return node
        if(newfmax != None):
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
        if newNode != None:
            return newNode, None
        if newLimit < min:
            min = newLimit
    return None, min


def printOutput(sol):
    global goal, n
    print("SUCCESS\n")
    path = []
    while(sol != None):
        path.insert(0, sol)
        sol = sol.parent
    for i in range(len(path)):
        state = path[i]
        for j in range(n):
            for k in range(n):
                if(k < n-1):
                    print((state.tiles)[j][k] + " ", end="")
                else:
                    print((state.tiles)[j][k])
        print("\n"),


def solve():
    global depth, n, goal, start
    getInput()
    solution = None
    solution = IDAstar()

    if(solution == None):
        print("FAILURE")
    else:
        printOutput(solution)


solve()
