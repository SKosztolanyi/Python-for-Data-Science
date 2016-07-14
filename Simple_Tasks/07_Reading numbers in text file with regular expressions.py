import re

text1 = open("regex_sum_42.txt")
allnumbers = []
for line in text1:
    line = line.rstrip()
    charnumbers = re.findall("[0-9]+", line)
    for char in charnumbers:
        number = int(char)
        allnumbers.append(number)
print sum(allnumbers)
        
        
text2 = open("regex_sum_167931.txt")
allnumbers2 = []
for line in text2:
    line = line.rstrip()
    charnumbers = re.findall("[0-9]+", line)
    for char in charnumbers:
        number = int(char)
        allnumbers2.append(number)
print sum(allnumbers2)
        