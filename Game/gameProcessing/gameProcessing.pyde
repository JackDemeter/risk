""" Game idea

Using graphing and nodes we can create the game of risk, where each node points
to a country class, these classes would hold the position the connections, the
piece would be displayed ontop of a photo of a predone risk field

Variables   type        Purpose                                                 Value
playerTurn        int/bool    value holds up to four players(might make it 1)         0 <= x <= 4
frame       int         holds the current frame that should be displayed
mouse       bool        switch for if the mouse is pressed                      true false
stage       int         what step of the play we are in similar to frame        0 <= x <= 10
attacker
defender    refrence    both refer to a class, the attacker and defender for fights
winCheck    int         checks if the player has one and reset the field       int 


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

#________________________________ Imports ______________________________________


#import math to do mouse to a point calculations
import math
#import random for the dice rolling
import random





#_____________________________________ Classes _________________________________


       
        
#creates a graph to allow linking between the different classes
class Graph():
    

    def __init__(self):
        self.size = 0
        self.vertices = {}
        self.neighbours = 0

    def numVertices(self):
        return self.size

    def addVertex(self,name, value):
        #prevents duplication from user
        if name not in self.vertices:
            #creates a dict value
            self.vertices[name] = value
            self.neighbours += 1
            return True
        return False

    def findNode(self, name):
        #looks in the dict if the value exists
        if name in self.vertices:
            #returns the class to the caller
            return self.vertices[name]
        return None

    def addNeighbour(self, objA, objB):
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
    def __init__(self, continent , troops, xPos, yPos, team):
        #a value holding the location of the place
        #if a user owns all nodes of a continent then they gain more troops
        self.continent = continent
        #how many troops they have
        self.troops = troops
        #the position to display on the screen
        self.x = xPos
        self.y = yPos
        self.team = team
        #when the data is reset
        self.resetData = [continent, troops, xPos, yPos, team]
        self.radius = 10
        self.neighbours = {}
        self.num = 0
    
    

    def addNeighbour(self, name, value):
        if name not in self.neighbours:
            #adds a new neigbour to the vertex
            self.neighbours[name] = value
            self.num+=1
            return True
        return False

    def removeNeighbour(self, name):
        if name in self.neighbours:
            #deletes a neigbour to the vertex
            del self.neighbours[name]
            self.num -= 1
            return True
        return False
    
    
    
    #used for playing
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
    
    def deadTroops(self, amount):
        self.troops -= amount
    
    def reset(self):
        #resets to the data it is initialized with
        self.country = self.resetData[0]
        self.troops = self.resetData[1]
        self.xPos = self.resetData[2]
        self.yPos = self.resetData[3]
        self.team = self.resetData[4]
        
    def inRange(self, mouseXVal, mouseYVal):
        #finds if the mouse is in p
        return (math.sqrt(abs(mouseXVal-self.x)**2+abs(mouseYVal-self.y)**2) < self.radius)
        
        
    def display(self,mouseXVal, mouseYVal):
        #if the team is 0 then the colour will not change/remain red
        global count
        fill(255,0,0)
        if self.team == 1:
            fill (0,255,0)
        elif self.team == 2:
            fill (0,0,255)
        elif self.team == 3:
            fill (255,255,0)
        #creates the circle
        ellipseMode(CENTER)
        ellipse(self.x, self.y, self.radius*2, self.radius*2)
        
        #if a vertex is scrolled over shows all the data in bottom corner
        if self.inRange(mouseXVal,mouseYVal):
            self.showStats(0, height-150)
            
    def teamClick(self, mouseXVal,mouseYVal, mouse, team):
        return self.inRange(mouseXVal,mouseYVal) and mouse and self.team == team
            
    def enhance(self):
        fill(0)
        ellipse(self.x,self.y,self.radius*2 + 2, self.radius*2 + 2)               
    
    def showStats(self,x,y):
        #displays in the based on x, y
        textBox(x, y, 200,150,0,150,CORNER)
        textSetup(menuFont, 35, CENTER, 255)
        text("Stats", x+100, y+15)
        #sets the text to left so they are flush, shows all stats of a vertex
        textSetup(menuFont, 30, LEFT, 255)
        text("team: ", x+10, y+40)
        text("troops: ", x+10, y+70)
        text("country: ", x+10, y+100)
        text("nb: ", 10, y + 130)
        text(self.team+1, x+170, y+40)
        text(self.troops, x+170, y+70)
        text(self.continent, x+170, y+100)
        text(self.num, x+170, y+130)
        

#creates a button based on given positions
class Button():
    def __init__(self, x, y, wide, tall, word, value, fontSize, fontType):
        #data for the rect
        self.x = x
        self.y = y
        self.wide = wide
        self.tall = tall
        #data for the text
        self.fontSize = fontSize
        self.fontType = fontType
        self.word = word
        #what value is returned if the button is clicked
        self.value = value
        
    
    def display(self, mousePosX, mousePosY):
        strokeWeight(1)
        stroke(0,0,0)
        fill(150,0,0)
        if self.inRange(mousePosX, mousePosY):
            fill(160,0,0)
        rectMode(CENTER)
        rect(self.x,self.y,self.wide,self.tall)
        fill(255)
        textFont(self.fontType)
        textAlign(CENTER,CENTER)
        textSize(self.fontSize)
        text(self.word,self.x,self.y)
        
    def inRange(self, mousePosX, mousePosY):
        return abs(mousePosX - self.x) <= self.wide / 2  and abs(mousePosY - self.y) <= self.tall/2
   
    def changeValue(self, mousePosX, mousePosY, mouse):
        #import frame to change the value directly(generally use pointers)
        global frame
        if self.inRange(mousePosX, mousePosY) and mouse:
            frame = self.value
    
    def givenValue(self, mousePosX, mousePosY, mouse,value, newValue):
        if self.inRange(mousePosX, mousePosY) and mouse:
            return newValue
        return value

    

#_________________________________________ FUNCTIONS ________________________________________

def countTroops(turn, world):
    #how many troops they should be given
    additional = 0
    #to check if they own a whole continent 
    continents = [0 for i in range(6)]
    maxC = [9,6,4,7,12,4]
    reward = [5,3,2,5,7,2]
    #each country gets the player a troop
    for i in world.vertices:
        if world.vertices[i].team == turn:
           additional+=0.5
           continents[world.vertices[i].continent] += 1
    #owning a continent grants bonus troops
    for i in range(6):
        if continents[i] == maxC[i]:
            additional += reward[i]
    return int(additional)
           

        
def calcWin(listA, listB):
    #compares the 2 lists comparing indices
    wins = 0
    for i in range(min(len(listA),len(listB))):
        #must be greater than, otherwise the defender wins
        if listA[i] > listB[i]:
            wins += 1
    return wins       



def scores(attacker, defender):
    troopA = attacker.troops
    troopB = defender.troops
    #attackers must have atleast one troop staying behind 
    #attacker can only use 3 at max
    if troopA > 4:
        troopA = 4
    troopA = troopA - 1
    #defender can only have 2 at a time
    if troopB > 2:
        troopB = 2
    #depending on the amount of troops that you have it will give you a random dice roll
    oddsA = []
    for i in range(troopA):
        oddsA.append(random.randint(0,6))
    oddsB = []
    for i in range(troopB):
        oddsB.append(random.randint(0,6))
    #sorts lists 
    oddsA.sort()
    oddsB.sort()
    #reverses order to make largest appear first
    oddsA.reverse()
    oddsB.reverse()
    return [oddsA, oddsB]




#_________________________________ DISPLAY FUNCTIONS ________________________________________

def displayHome(buttons, font, mouse):
    #fades adn creates title
    fadeBG(100, 120)
    textBox(width/2, height/2, 400, 600, 100, 200)
    textSetup(font, 60)
    text("Menu", width/2, height/2 - 220 )
    fill(255,200)
    
    #displays all the buttons associated with the home page
    buttonDisplay(buttons)
    
    
    
def displayAttack(font, atD):
    #creates a text box showing the stats of the attacker and defender
    fadeBG(100,120)
    textBox(width/2, height/2, 600, 600, 100, 200)
    textSetup(font, 60)
    text ("attack", width/2 - 150, height/2 - 220)
    text ("defend", width/2 + 150, height/2 - 220)
    for i in range(len(atD[0])):
        text(str(atD[0][i]), width/2-150, height/2+50 * i)
    for i in range(len(atD[1])):
        text(str(atD[1][i]), width/2+150, height/2+50 * i)
    for i in range(max(len(atD[0]),len(atD[1]))):
        strokeWeight(10)
        line(width/2+50,height/2 + 50 * i,width/2-50,height/2 + 50 * i)
    
                
                    
def displayHow(buttons,font, howTo, mouse):
    #fades background
    fadeBG(100, 120)
    textBox(width/2, height/2, 800, 600, 100, 200)
    #writes the title
    textSetup(font, 60)
    text("How To Play", width/2, height/2 - 220 )
    #adds the white text box
    textBox(width/2, height/2+50, 700, 400, 230, 255)
    #reduces font size
    textSetup(font, 26, LEFT)
    #reads in the howTo.txt file and prints based on lines in the file
    for i in range(len(howTo)):
        text(howTo[i], width/2 - 300, height/2 - 120 + 30*i)
    #displays all the buttons associated with the how to page
    #for how to it is only the back page
    buttonDisplay(buttons)



def displayPlay(buttons, font, turn, world, mouseXVal,mouseYVal):
    #displays all of the nodes and allows you to look at the information
    textSetup(font, 40)
    text("Turn: ", 1000,50)
    text(turn+1, 1080,50)
    buttonDisplay(buttons)
    for i in world.vertices:
        world.vertices[i].display(mouseXVal, mouseYVal)



def fadeBG(colour, fade):
    #places a faded rect into cover the whole background for a nice effect
    fill(colour,fade)
    strokeWeight(0)
    rectMode(CORNER)
    rect(0,0,width,height)



def textBox(centerX, centerY, x, y, colour, fade, position = CENTER):
    #similar to fade background however creates a text box
    stroke(0)
    strokeWeight(1)
    fill(colour, fade)
    rectMode(position)
    rect(centerX, centerY, x,y)



def textSetup(font, fSize, position = CENTER, shade = 0):
    #crunches this 4 line basic setup into 1 line, independant text
    #sets the size and font to prevent previous code from affecting it
    textAlign(position,CENTER)
    fill(shade)
    textFont(font)
    textSize(fSize)
 
    
          
def buttonDisplay(buttons):
    for i in buttons:
        i.display(mouseX,mouseY)
        #changes the value is clicked
        i.changeValue(mouseX,mouseY, mouse)
  
        
                    
def whatStage(word, font, fSize):
    #displays the point in the game in the top corner
    textSetup(font, fSize)
    text(word, 1000,75)




#________________________________________ Built in Functions ___________________________________

def mouseReleased():
    #uses a global boolean switch that is turned true when clicked
    global mouse
    mouse = True
    
    
#_________________________________________ setup Loop ________________________________________




def setup():
    global mapPhoto, menuFont, howTo
    global world, homeButtons, howButtons, playButtons, endTurn, activate
    global mouse, playerTurn, frame, stage, count, attDef, cont, winCount
    #sets to size of photo
    size(1122,711)
    
    
    
    #loads all data
    mapPhoto = loadImage("gameBoard.jpg")
    menuFont = loadFont("start.vlw")
    #reads in the text files
    howTo = loadStrings("howTo.txt")
    points = loadStrings("mapping.txt")
    links = loadStrings("links.txt")
    
    

    #Button Classes, create buttons that change the location when clicked
    homeButtons = [Button(width/2, height/2-100, 350, 100, "Play", 1, 60, menuFont), 
                   Button(width/2, height/2+50, 350, 100, "Guide", 2, 60, menuFont),
                   Button(width/2, height/2+200, 350, 100, "Reset", 3, 60, menuFont)]
    howButtons =  [Button(220, 90, 100, 50, "Back", 0, 30, menuFont)]
    playButtons = [Button(50, 25, 100, 50, "Esc", 0, 30, menuFont)]
    
    endTurn =      Button(width - 50, height - 25, 100, 50, "End", 1, 30, menuFont)
    activate =     Button(width/2, height/3,150,50,"Attack", 1, 30, menuFont)
    cont =         Button(width/2, height/3,150,50,"Continue", 1, 30, menuFont)
    
    
    
    #set up the world vertices and edges using the data read from a file
    world = Graph()
    for i in points:
        #similar reading in the lines in the student database project
        i = i.strip()
        i = i.split(",")
        #creates all the "nodes" aka vertexs
        world.addVertex(str(i[0]),Place(int(i[1]),int(i[2]),int(i[3]),int(i[4]),int(i[5])))
        
    #links all the nodes together
    for i in links:
        i = i.strip()
        i = i.split(",")
        world.addNeighbour(i[0],i[1])
    
        

    #variables
    mouse = False
    playerTurn = 0
    stage = 0
    frame = 0
    count = 0
    attacker = None
    defender = None
    attDef = [[],[]]
    winCount = 0
  
    
#_________________________________________ draw Loop ________________________________________      
        
            
def draw():
    #imports 
    global mapPhoto, frame, home, menuFont, howTo
    #classes
    global world, homeButtons, howButtons, playButtons, endTurn, activate
    #variables
    global mouse, playerTurn, frame, stage, mouse, count, attacker, defender, attDef, cont, winCount
    #this background will be in all shots
    background(mapPhoto)
    
    if winCount == 3:
        #if the win counter skips 3 people in a row the 4th person must of won, prints winner and resets game
        print "WINNER!"
        stage = 3
    
    
    if frame == 0:
        displayHome(homeButtons, menuFont, mouse) 
        
        
        
    if frame == 1:
        #bool that turns on and off the places keypoints
        display = True
        
        
        if stage == 0:
            #calcs how many troops to add, gives it to a global variable moves to the next step
            count = countTroops(playerTurn,world)
            #if the troops are 0 then the person has no countries and is out of the game
            if count == 0:
                #turn is skipped, because they are out
                stage = 6
                winCount += 1
                #otherwise it goes to the next step
            stage += 1
            winCount = 0
            
            
        if stage == 1:
            #Adds troops in this process, 
            whatStage("Add Troops: ", menuFont, 20)
            #displays the number of troops left to add
            textSetup(menuFont, 30)
            text(count, width-40, 100 )
            #checks if the user clicks on a place that is part of his team
            for i in world.vertices:
                if world.vertices[i].teamClick(mouseX,mouseY,mouse, playerTurn):
                    world.vertices[i].addTroops(1)
                    count -= 1
            #sets the attacker to 0 to prevent potential bugs
            attacker = None
            defender = None
            if count == 0:
                stage = 2
                
                
        elif stage == 2:
            attDef = [[],[]]
            whatStage("Attack!", menuFont, 20)
            
            for i in world.vertices:
                if world.vertices[i].teamClick(mouseX,mouseY,mouse, playerTurn):
                    attacker = world.vertices[i]
                if attacker != None and attacker.troops > 1:
                    for neighbour in attacker.neighbours:
                        #shows dark circle around enemies
                        if attacker.neighbours[neighbour].team != playerTurn:
                            attacker.neighbours[neighbour].enhance()
                            if attacker.neighbours[neighbour].inRange(mouseX,mouseY) and mouse:
                                #if a person is clicked on we engage the attack
                                defender = attacker.neighbours[neighbour]
                                stage = 3
            endTurn.display(mouseX,mouseY)
            stage = endTurn.givenValue(mouseX,mouseY, mouse, stage, 6)                  
                                
                                            
        elif stage == 3:
            #this stage shows the attack
            displayAttack(menuFont, attDef)
            #turns off the diplay to prevent overlay
            display = False
            activate.display(mouseX,mouseY)
            stage = activate.givenValue(mouseX,mouseY, mouse, stage, 4)
            
            
        elif stage == 4:
            #returns a list that shows the list of attacker and defender
            displayAttack(menuFont, attDef)
            attDef = scores(attacker,defender)
            defender.deadTroops(calcWin(attDef[0],attDef[1]))
            attacker.deadTroops(min(len(attDef[0]),len(attDef[1])) - calcWin(attDef[0],attDef[1]))
            if defender.troops == 0:
                #moves the troops to the newly claimed land
                defender.team = playerTurn
                
                defender.addTroops(attacker.troops/2)
                attacker.deadTroops(attacker.troops/2)
                attacker = None
                defender = None
            stage = 5
            
            
        elif stage == 5:
            #shows all the data once the user attacks
            displayAttack(menuFont, attDef)
            display = False
            cont.display(mouseX,mouseY)
            stage = cont.givenValue(mouseX,mouseY, mouse, stage, 2)
            
            
        elif stage == 6:
            #changes the player turn and restarts the process
            playerTurn = (playerTurn + 1) % 4
            stage = 0
        if display:
            displayPlay(playButtons, menuFont, playerTurn, world, mouseX, mouseY)
          
            
                
    if frame == 2:
        #shows the how to bar
        displayHow(howButtons, menuFont, howTo, mouse)



    if frame == 3:
        #resets all the data to play a new game
        for i in world.vertices:
            world.vertices[i].reset()
        frame = 1
        playerTurn = 0
        stage = 0
        
    #sets the mouse to false so that once clicked the mouse cant be dragged and still open stuff
    mouse = False    
        
    