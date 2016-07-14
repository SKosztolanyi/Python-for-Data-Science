import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def vowelcount(words):
    proportions = []
    for word in words:
        vowels = 0
        for char in word:
            if char.upper() in ('A', 'E', 'I', 'O', 'U'):
                vowels += 1
            frequency = float(vowels)/len(word) 
            # needs to be float, otherwise gets rounded down to 0 as int
        proportions.append(frequency)
    return proportions
                  
def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    vowel_ratio = vowelcount(wordList)
    pylab.hist(vowel_ratio, bins = numBins)
    xmin,xmax = pylab.xlim()
    ymin,ymax = pylab.ylim()
    pylab.title('Proportion of vowels in each word from sample list')
    pylab.xlabel('Vowels in Words')
    pylab.ylabel('Number of words')
    
if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)

sample_words = loadWords()
test_words = ['slime', 'window', 'ook', 'inkilinkiiiiii']
#print vowelcount(test_words)
pylab.show()

