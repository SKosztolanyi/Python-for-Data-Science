import pylab

class Item(object): # creating a class for use in further functions
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', '\
                 + str(self.weight) + '>'
        return result

def buildItems(): # creates a list of items
    names = ['clock', 'painting', 'radio', 'vase', 'book',
             'computer']
    vals = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    return Items

def greedy(Items, maxWeight, keyFcn): # greedy algorithm 
    assert type(Items) == list and maxWeight >= 0
    ItemsCopy = sorted(Items, key=keyFcn, reverse = True)
    # The items are ordered according to keyFcn. sorted creates a copy of the list in ordered fashion
    # keyFcn can be changed and it will change an ordering, eg. according to value, weight, ratio, etc.
    result = []
    totalVal = 0.0
    totalWeight = 0.0
    i = 0
    while totalWeight < maxWeight and i < len(Items):
        if (totalWeight + ItemsCopy[i].getWeight()) <= maxWeight:
            result.append((ItemsCopy[i]))
            totalWeight += ItemsCopy[i].getWeight()
            totalVal += ItemsCopy[i].getValue()
        i += 1
    return (result, totalVal)

def value(item):
    return item.getValue()

def weightInverse(item):
    return 1.0/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()

def testGreedy(Items, constraint, getKey):
    taken, val = greedy(Items, constraint, getKey)
    print ('Total value of items taken = ' + str(val))
    for item in taken:
        print '  ', item

def testGreedys(maxWeight = 20):
    Items = buildItems()
    print('Items to choose from:')
    for item in Items:
        print '  ', item
    print 'Use greedy by value to fill a knapsack of size', maxWeight
    testGreedy(Items, maxWeight, value)
    print 'Use greedy by weight to fill a knapsack of size', maxWeight
    testGreedy(Items, maxWeight, weightInverse)
    print 'Use greedy by density to fill a knapsack of size', maxWeight
    testGreedy(Items, maxWeight, density)

# result:
#Items to choose from:
#   <clock, 175.0, 10.0>
#   <painting, 90.0, 9.0>
#   <radio, 20.0, 4.0>
#   <vase, 50.0, 2.0>
#   <book, 10.0, 1.0>
#   <computer, 200.0, 20.0>
#Use greedy by value to fill a knapsack of size 20
#Total value of items taken = 200.0
#   <computer, 200.0, 20.0>
#Use greedy by weight to fill a knapsack of size 20
#Total value of items taken = 170.0
#   <book, 10.0, 1.0>
#   <vase, 50.0, 2.0>
#   <radio, 20.0, 4.0>
#   <painting, 90.0, 9.0>
#Use greedy by density to fill a knapsack of size 20
#Total value of items taken = 255.0
#   <vase, 50.0, 2.0>
#   <clock, 175.0, 10.0>
#   <book, 10.0, 1.0>
#   <radio, 20.0, 4.0>

## There is still no guarantee, that greedy algorithm will find the optimal solution
## Complexity of this algorithm is O(n log n) - because of the sorted and iteration that is following


def dToB(n, numDigits):
    """requires: n is a natural number less than 2**numDigits
      returns a binary string of length numDigits representing the
              the decimal number n."""
    assert type(n)==int and type(numDigits)==int and n >=0 and n < 2**numDigits
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr # this way the number is added in front and not to back
        n = n//2
    while numDigits - len(bStr) > 0: 
    # if the lenght bstring is smaller than digits wanted, add zeros in front of string to the needed lenghts 
        bStr = '0' + bStr
    return bStr

def genPset(Items):
    """Generate a list of lists representing the power set of Items"""
    numSubsets = 2**len(Items) # We know the size of the power set based on count of items in list
    templates = []
    for i in range(numSubsets):
        # I create a binary representation of every subset with dToB functionge
        templates.append(dToB(i, len(Items)))
    pset = []
    for t in templates:
        elem = []
        for j in range(len(t)):
            if t[j] == '1':
                elem.append(Items[j])
        pset.append(elem)
    return pset

def chooseBest(pset, constraint, getVal, getWeight):
    # This is the brute force approach to knapsack problem
    # I have all the subsets of a set and I choose the one that best fits my criteria
    bestVal = 0.0
    bestSet = None
    for Items in pset:
        ItemsVal = 0.0
        ItemsWeight = 0.0
        for item in Items:
            ItemsVal += getVal(item)
            ItemsWeight += getWeight(item)
        if ItemsWeight <= constraint and ItemsVal > bestVal:
            bestVal = ItemsVal
            bestSet = Items
    return (bestSet, bestVal)

def testBest():
    # Uses all the helper functions above
    Items = buildItems()
    pset = genPset(Items)
    taken, val = chooseBest(pset, 20, Item.getValue, Item.getWeight)
    print ('Total value of items taken = ' + str(val))
    for item in taken:
        print '  ', item
        
# This solution always finds the best solution, but is really expensive because of the complexity O(2**n)

def maxVal(toConsider, avail): 
    # A recursive implementation of knapsack problem
    # uses binary desicion tree
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        result = maxVal(toConsider[1:], avail)
    # If this condition is True, then the left branch is empty and we consider only the right branch
    else:
        nextItem = toConsider[0]

        #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:],
                                      avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)

        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result
# This solution is cheaper than Brute Force, because it doesn't explore the whole power set
# As soon as the constraint is broken it stops the branch and goes to another branch

def smallTest():
    Items = buildItems()
    val, taken = maxVal(Items, 20)
    for item in taken:
        print(item)
    print ('Total value of items taken = ' + str(val))
    
#result:
#<book, 10.0, 1.0>
#<painting, 90.0, 9.0>
#<clock, 175.0, 10.0>
#Total value of items taken = 275.0


# Generator function:
def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as a list of which item(s) are in each bag.
    """
    N = len(items)
    # Enumerate the 3**N possible combinations   
    for i in xrange(3**N):
        bag1 = []
        bag2 = []
        for j in xrange(N):
            if (i / (3 ** j)) % 3 == 1:
                bag1.append(items[j])
            elif (i / (3 ** j)) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2) # yield returns a generator
# when I call the function, the code in the body of the function does not run. 
# The function only returns the generator object

test_items = buildItems()
combos = yieldAllCombos(test_items)