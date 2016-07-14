# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    population_at_end = []
    treatOnStep = 75 #, 0, 75, 150, 300
    steps = treatOnStep + 150
    #trialResultsTot = [[] for s in range(steps)]
    #trialResultsRes = [[] for s in range(steps)]
    for __ in range(numTrials):
        viruses = [ResistantVirus(maxBirthProb, clearProb, resistances.copy(), mutProb) for virus in range(numViruses)]
        patient = TreatedPatient(viruses, maxPop)
        for step in range(steps):
            if step == treatOnStep:
                patient.addPrescription("guttagonol")
            patient.update()
        final_viruses = patient.getTotalPop()
        population_at_end.append(final_viruses)
    #resultsSummaryTot = [sum(l) / float(len(l)) for l in trialResultsTot]
    #resultsSummaryRes = [sum(l) / float(len(l)) for l in trialResultsRes]
    #pylab.plot(resultsSummaryTot, label="Total Virus Population")
    #pylab.plot(resultsSummaryRes, label="Resistant Virus Population")
    #pylab.title("ResistantVirus simulation")
    #pylab.xlabel("time step")
    #pylab.ylabel("# viruses")
    #pylab.legend()
    pylab.xlabel('number of viruses')
    pylab.ylabel('Number of Trials')
    pylab.hist(population_at_end)
    pylab.show()


print simulationWithDrug(100, 1000, 0.1, 0.05, {"guttagonol": False}, 0.005, 400)




#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    population_at_end = []
    treatOnStep = 150 #, 0, 75, 150, 300
    treatOnStep2 = treatOnStep + 0 #, 0, 75, 150, 300
    steps = treatOnStep2 + 150
    #trialResultsTot = [[] for s in range(steps)]
    #trialResultsRes = [[] for s in range(steps)]
    for __ in range(numTrials):
        viruses = [ResistantVirus(maxBirthProb, clearProb, resistances.copy(), mutProb) for virus in range(numViruses)]
        patient = TreatedPatient(viruses, maxPop)
        for step in range(steps):
            if step == treatOnStep:
                patient.addPrescription("guttagonol")
                #print "guttanol added", step
            if step == treatOnStep2:
                patient.addPrescription("grimpex")
                #print "grimpex added", step
            patient.update()
        final_viruses = patient.getTotalPop()
        population_at_end.append(final_viruses)
    #resultsSummaryTot = [sum(l) / float(len(l)) for l in trialResultsTot]
    #resultsSummaryRes = [sum(l) / float(len(l)) for l in trialResultsRes]
    #pylab.plot(resultsSummaryTot, label="Total Virus Population")
    #pylab.plot(resultsSummaryRes, label="Resistant Virus Population")
    #pylab.title("ResistantVirus simulation")
    #pylab.xlabel("time step")
    #pylab.ylabel("# viruses")
    #pylab.legend()
    #print population_at_end
    pylab.xlabel('number of viruses')
    pylab.ylabel('Number of Trials')
    pylab.hist(population_at_end)
    pylab.show()

print simulationTwoDrugsDelayedTreatment(100, 1000, 0.1, 0.05, {'guttagonol': False, 'grimpex': False}, 0.005, 10) # for debugging  
simulationTwoDrugsDelayedTreatment(100, 1000, 0.1, 0.05, {'guttagonol': False, 'grimpex': False}, 0.005, 400)
