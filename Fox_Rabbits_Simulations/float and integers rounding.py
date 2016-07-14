import numpy

A = [0,1,2,3,4,5,6,7,8]

B = [5,10,10,10,15]

C = [0,1,2,4,6,8]

D = [6,7,11,12,13,15]

E = [9,0,0,3,3,3,6,6]

print numpy.mean(A)
print numpy.mean(B)
print numpy.mean(C)
print numpy.mean(D)
print numpy.mean(E)

print numpy.var(A)
print numpy.var(B)
print numpy.var(C)
print numpy.var(D)
print numpy.var(E)


def possible_mean(L):
    return sum(L)/len(L)

def possible_variance(L):
    mu = possible_mean(L)
    temp = 0
    for e in L:
        temp += (e-mu)**2
    return temp / len(L)
    
print possible_variance(A)
print possible_variance(B)
print possible_variance(C)
print possible_variance(D)
print possible_variance(E)

# The difference is caused by python float and integer rounding.