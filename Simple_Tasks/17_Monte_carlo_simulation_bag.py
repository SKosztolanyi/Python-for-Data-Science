import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    success = 0
    for i in range(numTrials):
        balls =""
        bag = ['R', 'R', 'R', 'G', 'G', 'G']
        for j in range(3):
            ball = random.choice(bag)
            bag.remove(ball)
            balls += ball
        #print balls
        print bag
        if balls == 'RRR' or balls == 'GGG':
            success += 1
    return success/float(numTrials)
    
print noReplacementSimulation(10)
            