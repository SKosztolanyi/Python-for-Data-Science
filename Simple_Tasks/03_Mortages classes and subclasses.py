# Plotting and calculating mortages

def findPayment(loan, r, m):
    """
    Assumes: loan and r are floats, m an int
    Returns the monthly payment for mortage of size
    loan at a monthly rate of r for m months
    """
    return loan * ((r*(1+r)**m)/((1+r)**m - 1))
    
class Mortage(object):
    """
    Abstract class for building different kinds of mortages
    """
    def __init__ (self, loan, annRate, months):
        self.loan = loan
        self.rate = annRate/12
        self.months = months
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None # description of mortage
        
    def makePayment(self):
        """
        Make payment
        """
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1]*self.rate
        self.owed.append(self.owed[-1] - reduction)
        
    def getTotalPaid(self):
        """Return the total amount paid so far"""
        return sum(self.paid)
        
    def __str__(self):
        return self.legend
        
# Fixed rate mortage        
class Fixed(Mortage):
    def __init__(self, loan, r, months):
        Mortage.__init__(self, loan, r, months)
        self.legend = "Fixed, " + str(r*100) + "%"
        
# fixed-rate mortage with up-front points
class FixedWithPts(Fixed):
    def __init__(self, loan, r, months, pts):
        Fixed.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan*(pts/100)]
        self.legend += "," + str(pts) + " points"
        
# mortage that changes interest rate after 48 months
class TwoRate(Mortage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortage.__init__(self, loan, teaserRate, months)
        self.teaserRate = teaserRate
        self.teaserMonths = teaserMonths
        self.nextRate = r/12
        self.legend = str(teaserRate*100)\
            + "% for" + str(self.teaserMonths)\
            + "months, then " + str(r*100) + "%"
            
    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate
            self.payment = findPayment(self.owed[-1], self.rate, self.months - self.teaserMonths)
        Mortage.makePayment(self)
        
# Helper function to try out alternatives
def compareMortages(amt, years, fixedRate, pts, ptsRate, varRate1, varRate2, varMonths):
    totMonths = years * 12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
    morts = [fixed1, fixed2, twoRate]
    
    # running experiment
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
            
    # reporting results
    for m in morts:
        print m
        print "Total payment = $" + str(int(m.getTotalPaid()))
        
        
# amount borrowed : $ 200,000
# term: 30 years
# option 1: rate = 7%
# option 2: 3.25 points upfront, rate = 5%
# option 3: 48 months of rate = 5%, then rate = 9.5%

"""
compareMortages(amt = 200000, years = 30, fixedRate = 0.07, pts = 3.25, ptsRate = 0.05,varRate1 = 0.045, varRate2 = 0.095, varMonths = 48)
"""        
        
               