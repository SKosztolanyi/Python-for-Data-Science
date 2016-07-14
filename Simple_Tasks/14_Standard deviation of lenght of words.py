# -*- coding: utf-8 -*-
def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    length = 0
    diffs = 0
    if len(L) == 0:
        return float('NaN')
    for element in L:
        length += len(element)
    mean = float(length) / len(L)
    # I need to use floats, otherwise it gets automatically converted into ints during the computations
    #print mean
    for every in L:
        diffs += (len(every) - mean)**2
        #print diffs
    square_dev = (diffs/len(L))**0.5
    return square_dev
    #    
    #∑t in X(t−μ)2
    #That is, for each element (that we name t) in the set X,
    #we compute the quantity (t−μ)2. 
    #We then sum up all those computed quantities.
    #N is the number of elements in X