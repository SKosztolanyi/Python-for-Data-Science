import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    random.seed(0)
    det = random.randint(10, 20)
    if det % 2 != 0:
        det += 1
    return det
    
def deterministicNumber2():
    random.seed(1)
    return 2*random.randint(5, 10)
    #one line solution that is more compact
    
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    fuss = random.randint(10, 20)
    if fuss % 2 != 0:
        fuss += 1
    return fuss