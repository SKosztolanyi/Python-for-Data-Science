import pylab

# plotting an investment
principal = 1000
interest_rate = 0.05
years = 20
values = []
for i in range (years + 1):
    values.append(principal)
    principal += interest_rate * principal
pylab.plot(range(years+1), values, "ro", ) # changing color to red and line to circles
pylab.title("5% growth, Compounded Annualy")
pylab.xlabel("Years of compounding", fontsize = 12)
pylab.ylabel("Value of principal($)", fontsize = 10)
pylab.show()

# This plot is without labels and names and therefore is uninformative,
# therefore we added title and labels