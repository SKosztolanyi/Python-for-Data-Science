import random

# Probability is a float number between 0 and 1.
# 0 is never occuring, 1 is always occuring

def rollDie():
    return random.choice([1,2,3,4,5,6])

# how many times will I roll a die
def rollN(n):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    return result

print rollN(5)

# Goal should be written as a string, consisting of numberst 1 to 6
def getTarget(goal):
    numTries = 0
    numRolls = len(goal)
    while True:
        numTries += 1
        result = rollN(numRolls)
        if result == goal:
            return numTries

#This function calculates the mean of number of tries before getting to the goal
#The bigger number of trials I choose, the closer I get to the expected probability mathematicaly calculated
#This shows the law of big numbers
def runSim(goal, numTrials):
    total = 0
    for i in range(numTrials):
        total += getTarget(goal)
    print 'Average number of tries =', total/float(numTrials)

##runSim('11111', 100)
##runSim('54324', 100)

# What is the probability, that there will be at least one one in the die rolls?
def atLeastOneOne(numRolls, numTrials):
    numSuccess = 0
    for i in range(numTrials):
        rolls = rollN(numRolls)
        if '1' in rolls:
            numSuccess += 1
        fracSuccess = numSuccess/float(numTrials)
    print fracSuccess

atLeastOneOne(10, 1000)