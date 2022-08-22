'''
You have a set of unlabeled foods to eat and you attempt to identify what each item is. The probability of guessing each food correctly is in the list probs. You make a guess for every food and you pay cost dollars per guess. For each food you identify correctly, you receive get dollars. Write a Monte Carlo simulation that runs num_trials number of trials of this guessing game.

More specifically, write a function according to the specifications below (you are also given a helper function):

# helper function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std  
  
def guessfood_sim(num_trials, probs, cost, get):
    """
    num_trials: integer, number of trials to run
    probs: list of probabilities of guessing correctly for 
           the ith food, in each trial
    cost: float, how much to pay for each food guess
    get: float, how much you get for a correct guess
    
    Runs a Monte Carlo simulation, 'num_trials' times. In each trial 
    you guess what each food is, the ith food has 'prob[i]' probability 
    to get it right. For every food you guess, you pay 'cost' dollars.
    If you guess correctly, you get 'get' dollars. 
    
    Returns: a tuple of the mean and standard deviation over 
    'num_trials' trials of the net money earned 
    when making len(probs) guesses
    """

You are not allowed to import anything besides random. If you use the helper function, paste that in the code box as well. Do not leave any debugging print stataments. Click "See full output" to see the test cases passed/failed. Paste only the guessfood_sim function and any helper functions you made for yourself (if any).

'''
import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    # TODO
    pylab.hist(values, bins = numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title != None:
        pylab.title(title)
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """
    # TODO
    longest_runs = []
    for i in range(numTrials):
        rolls = [die.roll() for j in range(numRolls)]
        size = 1
        max_size = 0
        for i in range(len(rolls)-1):
            if rolls[i+1] == rolls[i]:
                size += 1
            else: 
                size = 1
            if max_size < size:
                max_size = size
        if max_size > 0:
            longest_runs.append(max_size)
        else:
            longest_runs.append(1)
    makeHistogram(longest_runs, numBins = 10, xLabel = 'Length of longest run', yLabel = 'frequency', title = 'Histogram of longest runs')
    return sum(longest_runs)/len(longest_runs)
        
    
# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))
print(getAverage(Die([1,2,3,4,5,6]), 50, 1000))
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 1, 1000))