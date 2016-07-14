class Location(object):
    
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'





class Field(object):
    
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


import random


class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name
    
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


def walk(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(start.distFrom(f.getLoc(d)))



def simWalks(numSteps, numTrials):
    homer = UsualDrunk('Homer')
    notOrigin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, notOrigin)
        distances.append(walk(f, homer, numSteps))
    return distances



def drunkTest(numTrials = 20):
    #If I want a reproducible result I add:
    random.seed(0) #- pseudo random choices
    for numSteps in [10, 100, 1000, 10000]:
        distances = simWalks(numSteps, numTrials)
        print 'Random walk of ' + str(numSteps) + ' steps'
        print ' Mean =', sum(distances)/len(distances)
        print ' Max =', max(distances), 'Min =', min(distances)

import pylab
        
def drunkTestP(numTrials = 50):
    stepsTaken = [10, 100, 1000, 10000]
    meanDistances = []
    for numSteps in stepsTaken:
        distances = simWalks(numSteps, numTrials)
        meanDistances.append(sum(distances)/len(distances))
    pylab.plot(stepsTaken, meanDistances)
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.show()
    
# Is there some relationship between distance from origin and steps taken?
# We can try square root of steps taken to see how it relates to the distance.

def drunkTestP1(numTrials = 50):
    stepsTaken = [10, 100, 1000, 10000]
    meanDistances = []
    squareRootOfSteps = []
    for numSteps in stepsTaken:
        distances = simWalks(numSteps, numTrials)
        meanDistances.append(sum(distances)/len(distances))
        squareRootOfSteps.append(numSteps**0.5)
    pylab.plot(stepsTaken, meanDistances, 'b-',
               label = 'Mean distance')
    pylab.plot(stepsTaken, squareRootOfSteps, 'g-.',
               label = 'Square root of steps')
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.legend()
    pylab.show()
    
# The two lines are not identical, but they are pretty close
# There is certainly a relationship between those two variables

# We now change the parameters of drunk to get different results:
class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,0.95), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

# Euclidean drunk can move diagonally
class EDrunk(Drunk):
    def takeStep(self):
        deltaX = random.random()
        if random.random() < 0.5:
            deltaX = -deltaX
        deltaY = random.random()
        if random.random() < 0.5:
            deltaY = -deltaY
        return (deltaX, deltaY)
        
class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,0.9), (0.0,-1.03), (1.03, 0.0), (-1.03, 0.0)]
        return random.choice(stepChoices)


import math

class EDrunk(Drunk):
    def takeStep(self):
        ang = 2 * math.pi * random.random()
        length = 0.5 + 0.5 * random.random()
        return (length * math.sin(ang), length * math.cos(ang))

class PhotoDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.0, 0.5),(0.0, -0.5),
                     (1.5, 0.0),(-1.5, 0.0)]
        return random.choice(stepChoices)

class DDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.85, 0.85), (-0.85, -0.85),
                     (-0.56, 0.56), (0.56, -0.56)] 
        return random.choice(stepChoices)

# The first simWalks had hardcoced usual drunk
# Now we change this class to contain new variable called dClass:

def simWalks2(numSteps, numTrials, dClass):
    homer = dClass('Homer')
    origin = Location(0, 0)
    distances = []
    coordinates = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numSteps))
        coordinates.append(f.getLoc(homer))
        #print coordinates
    return distances
    
def drunkTestPlot2(numTrials = 50):
    stepsTaken = [10, 100, 1000, 10000]
    for dClass in (UsualDrunk, ColdDrunk, EDrunk, PhotoDrunk, DDrunk):
        meanDistances = []
        for numSteps in stepsTaken:
            distances = simWalks2(numSteps, numTrials, dClass)
            meanDistances.append(sum(distances)/len(distances))
        pylab.plot(stepsTaken, meanDistances,
                   label = dClass.__name__)
        pylab.title('Mean Distance from Origin')
        pylab.xlabel('Steps Taken')
        pylab.ylabel('Steps from Origin')
        pylab.legend(loc = 'upper left')
    pylab.show()
    

def simWalks3(numSteps, numTrials, dClass):
    homer = dClass('Homer')
    origin = Location(0, 0)
    distances = []
    coordinates = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numSteps))
        coordinates.append(f.getLoc(homer))
        #print coordinates
    return coordinates

import matplotlib
        
def walkVector(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(f.getLoc(d).getX() - start.getX(),
           f.getLoc(d).getY() - start.getY())
           
def drunkTestPlot3(numTrials = 100):
    dClass = UsualDrunk #ColdDrunk UsualDrunk ,EDrunk , PhotoDrunk, DDrunk):
    for i in range(numTrials):
        homer = dClass('Homer')
        origin = Location(0, 0)
        coordinates = []
        f = Field()
        f.addDrunk(homer, origin)
        final_location = walkVector(f, homer, 5000)
        coordinates.append(final_location)
        x,y = zip(*coordinates)
        matplotlib.pyplot.scatter(x, y)
        
# This function makes a scatterplot for number of dots equal to num of trials,
# and shows final location for the trial for the type of drunk 
# Dalo by sa to upravit na 5 plotov alebo 1 plot s roznymi farbami, napr podla DTP2