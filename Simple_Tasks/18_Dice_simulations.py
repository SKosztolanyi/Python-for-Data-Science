import random

def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])

def checkPascal(numTrials, roll):
    '''
    This function counts the simulated probability of not throwing double six with two die in number of trials.
    roll is specifig die roll used in this function.
    Different dice (sided or not fair) produce different results.
    '''
    yes = 0.0
    for i in range(numTrials):
        for j in range(24):
            d1 = roll()
            d2 = roll()
            if d1 == 6 and d2 == 6:
                yes += 1
                break
    print 'Probability of losing =', 1.0 - yes/numTrials

##checkPascal(10000, rollDie)


def rollLoadedDie():
    if random.random() < 1.0/5.5:
        # This is not a fair dice, but a dice slightly favouring six
        return 6
    else:
        return random.choice([1,2,3,4,5])

##checkPascal(10000, rollLoadedDie)

def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        # simulating probability of tossing a head
        if random.random() < 0.5:
            heads += 1
    return heads/float(numFlips)

for i in range(5): #number of trials
    print flip(10)
