import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    #Do not import or use functions or methods from pylab, numpy, or matplotlib.
    #Do not leave any debugging print statements when you paste your code in the box.
    success = 0
    for pick in range(numTrials):
        bucket = ['R', 'G','G', 'G', 'G', 'R', 'R', 'R']
        tries = []
        for ball in range(3):
            out = random.choice(bucket)
            tries.append(out)
            bucket.remove(out)
        if tries == ['G', 'G', 'G'] or tries == ['R', 'R', 'R']: 
            success += 1
    return success/float(numTrials)
    
print drawing_without_replacement_sim(10000)

# The equation is 3/7*1/3 = 0.142 or 1/7