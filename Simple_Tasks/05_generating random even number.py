import random

def genEven():
    return random.randrange(0, 100, 2)

def genEven1():
    return random.choice(range(0, 100, 2))

def genEven2():
    return int(random.random() * 50)*2

def genEven3():
    return random.choice(range(0, 50))*2

def genEven4():
    x = random.randint(0, 98)
    while x % 2 != 0:
        x = random.randint(0, 98)
    return x