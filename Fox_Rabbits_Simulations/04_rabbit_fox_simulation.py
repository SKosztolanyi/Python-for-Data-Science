import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    
    for rabbit in range(CURRENTRABBITPOP):
        prob_rabbit_reproduction = 1.0 - (float(CURRENTRABBITPOP)/MAXRABBITPOP)
        if prob_rabbit_reproduction > random.random():
            CURRENTRABBITPOP += 1
        #else:
            #print rabbit, 'no born'
    #return CURRENTRABBITPOP
        
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    
    
    for fox in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP > 10:
            prob_fox_eats_rabbit = float(CURRENTRABBITPOP)/MAXRABBITPOP
            if prob_fox_eats_rabbit > random.random():
                CURRENTRABBITPOP -= 1
                if 1.0/3.0 > random.random():
                    CURRENTFOXPOP += 1
            elif CURRENTFOXPOP > 10:
                if 0.9 > random.random():
                    CURRENTFOXPOP -= 1
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations = []
    fox_populations = []
    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return (rabbit_populations, fox_populations)
    
def polyfitplot(numSteps):
    rabbits, foxes = runSimulation(numSteps)
    x_line = range(0, numSteps)
    rabbitVals = pylab.array(rabbits)
    foxVals = pylab.array(foxes)
    pylab.plot(x_line, rabbitVals, 'bo', label = 'rabbits') 
    pylab.plot(x_line, foxVals, 'r+', label = 'foxes')
    pylab.title('Change in animal populations across time')
    pylab.xlabel('Number of steps')
    pylab.ylabel('Population of foxes and rabbits')
    pylab.legend(loc = 'best')
    #pylab.show()
    coeff_rabbits = pylab.polyfit(range(len(rabbits)), rabbits, 2)
    pylab.plot(pylab.polyval(coeff_rabbits, range(len(rabbits))))
    pylab.title('Second order polynomial fit for rabbits')
    #pylab.show()
    coeff_foxes = pylab.polyfit(range(len(foxes)), foxes, 2)
    pylab.plot(pylab.polyval(coeff_foxes, range(len(foxes))))
    pylab.title('Second order polynomial fit for foxes')
    pylab.show()    
    
print polyfitplot(200)

