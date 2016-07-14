import string # for reading a string and slicing
import pylab # for plotting
import numpy # for manipulating lists

def loadtemperature():
    inFile = open("C:\Users\stefan\Google Drive OldZZZ\Coursera\Data Science\Into to Data Science with Python\julyTemps.txt", 'r')
    #line = inFile.read() - useless
    #print "  ", len(fields), "words loaded."
    #print fields
    low = []
    high = []
    for line in inFile:
        fields = line.split(" ")
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            low.append(int(fields[2])) # I need to change it to int as it appends a str
            high.append(int(fields[1]))
            #print line  
    #print low
    #print high 
    #print high[1] - low[1]
    return (low, high)
    
temperatures = loadtemperature()
print temperatures[1]

temperatures = loadtemperature()
highTemps = temperatures[1]
lowTemps = temperatures[0]
#print lowTemps
#print highTemps
diffTemps = list(numpy.array(highTemps) - numpy.array(lowTemps))
#print diffTemps

def producePlot(lowTemps, highTemps):
    """
    This function produces plot for temperatures differences.
    """   
    diffTemps = list(numpy.array(highTemps) - numpy.array(lowTemps))
    pylab.title ("Day by Day Ranges in Temprature in Boston in July 2012")
    pylab.ylabel("Temperature Ranges")
    pylab.xlabel("Days")
    pylab.plot(range(1,32), diffTemps)
    pylab.show()

(lowT, highT) = loadtemperature()    
producePlot(lowT, highT)        