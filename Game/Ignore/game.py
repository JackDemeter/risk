""" Game idea

Using graphing and nodes we can create the game of risk, where each node points
to a country class, these classes would hold the position the connections, the
piece would be displayed ontop of a photo of a predone risk field

Variables   type        Purpose                                                 Value
Turn        int/bool    value holds up to four players(might make it 1)         0 <= x <= 4




Class       Purpose

Linked      To create a linklist of multiple values that would be connected with neighbour edges
    Variables   type        Purpose                                                 Value
    countries   int         Holds the number of nodes that exists                   x >= 0
    root        class       pointer to the first value

    Function    Purpose
    add()       add a new node
    search()    looks for a value in the list using  breadth first search
    showNeighbours() Displays all the neighbour functions

"""


#creates a graph to allow linking between the different classes
class Graph():
    class Vertex():
        def __init__(self, value):
            self.value = value
            #has a list of all the neighbours of a vertex
            self.neighbours = {}

        def getNeighbours(self):
            return self.neighbours

        def getValue(self):
            return self.value

        def addNeighbour(self, name, value):
            if name not in self.neighbours:
                #adds a new neigbour to the vertex
                self.neighbours[name] = value
                return True
            return False

        def removeNeighbour(self, name):
            if name in self.neighbours:
                #deletes a neigbour to the vertex
                del self.neighbours[name]
                return True
            return False

    def __init__(self):
        self.size = 0
        self.vertices = {}

    def numVertices(self):
        return self.size

    def addVertex(self,value, name):
        #prevents duplication from user
        if name not in self.vertices:
            #creates a dict value
            self.vertices[name] = value
            return True
        return False

    def findNode(self, name):
        #looks in the dict if the value exists
        if name in self.vertices:
            #returns the class to the caller
            return self.vertices[name]
        return None

    def createNeighbour(self, objA, objB):
        #error check to make sure the data can be accessed
        if objA in self.vertices and objB in self.vertices:
            #this portion adds the neighbours to each other, since it is unidirectional
            self.vertices[objA].addNeighbour(objB, self.vertices[objB])
            self.vertices[objB].addNeighbour(objA, self.vertices[objA])
            #return if successful
            return True
        return False

    def removeNeighbour(self,objA, objB):
        if objA in self.vertices and objB in self.vertices:
            #this portion removes he neighbours from each other, since it is unidirectional
            #returns if the operation succeeded
            return self.vertices[objA].removeNeighbour(objB) and self.vertices[objB].removeNeighbour(objA)
        return False




#acts as the node to display the country or team etc
class Place():
    def __init__(self, country, troops, xPos, yPos, team):
        #a value holding the location of the place
        #if a user owns all nodes of a country then they gain more troops
        self.country = country
        #how many troops they have
        self.troops = troops
        #the position to display on the screen
        self.xPos = xPos
        self.yPos = yPos
        self.team = team
        #when the data is reset
        self.resetData = [country, troops, xPos, yPos, team]

    def teamSwap(self, team):
        self.team = team

    def moveTroops(self, place, amount):
        #must have atleast one troop
        #can only donate to neighbours
        if self.troops > amount:
            place.troops += amount
            self.troops -= troops

    def addTroops(self, amount):
        #At the beginning of each turn players allocate troops to locations
        self.troops += amount

    def reset(self):
        #resets to the data it is initialized with
        self.country = self.resetData[0]
        self.troops = self.resetData[1]
        self.xPos = self.resetData[2]
        self.yPos = self.resetData[3]
        self.team = self.resetData[4]



