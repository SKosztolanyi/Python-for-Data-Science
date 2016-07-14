import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    if title != None:
        pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel) 
    pylab.hist(values, bins = numBins)
    pylab.show()
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """ 
    longest = []
    longroll = 1
    for trial in range(numTrials):
        streak = 1
        rolled = []
        for rolls in range(numRolls):
            roll = die.roll()
            #print 'roll is', roll
            rolled.append(roll)
            if len(rolled) >= 2:
                if roll == rolled[-2]:
                    #print 'roll', roll, 'is', rolled[-1]
                    streak += 1
                else:
                    streak = 1                
                if streak > longroll:
                    longroll = streak
        longest.append(longroll)#print longroll
        longroll = 1
    mean = sum(longest)/float(len(longest))
    #print longest
    makeHistogram(longest, 10, 'longestRuns', 'numberOfTrials', 'histogram')
    return mean
    
# One test case
print getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000)
print getAverage(Die([1]), 10, 1000) # jeden krat je tam 9 a neviem preco
print getAverage(Die([1, 1]), 10, 1000) # jeden krat je tam 9 a neviem preco
print getAverage(Die([1,2,3,4,5,6,6,6,7]), 1, 1000)

# Previous version:
#def getAverage(die, numRolls, numTrials):
#    """
#      - die, a Die
#      - numRolls, numTrials, are positive ints
#      - Calculates the expected mean value of the longest run of a number
#        over numTrials runs of numRolls rolls.
#      - Calls makeHistogram to produce a histogram of the longest runs for all
#        the trials. There should be 10 bins in the histogram
#      - Choose appropriate labels for the x and y axes.
#      - Returns the mean calculated
#    """ 
#    rolled = []
#    longest = []
#    longroll = 1
#    for trial in range(numTrials):
#        streak = 1
#        for rolls in range(numRolls):
#            roll = die.roll()
#            #print 'roll is', roll
#            rolled.append(roll)
#            if len(rolled) > 1:
#                if roll == rolled[-2]:
#                    #print 'roll', roll, 'is', rolled[-1]
#                    streak += 1
#                else:
#                    streak = 1                
#                if streak > longroll:
#                    longroll = streak
#                    #print longroll
#        longest.append(longroll)
#        longroll = 1 
#    mean = sum(longest)/float(len(longest))
#    makeHistogram(longest, 10, 'longestRuns', 'numberOfTrials', 'histogram')
#    return mean