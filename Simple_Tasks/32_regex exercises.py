import re

def is_integer1(string):
    kon = re.search(r'-?\d+', string)
    bon = re.search(r'-?\w+', string)
    fon = re.search(r'-?\d{2, 1000}', string)
    return (kon.group(0), bon.group(0), fon.group(0))
    
def is_integer(string):
    return bool(re.match(r'^-?[0-9]*$', string))
    
print is_integer("42")         # True
print is_integer("-4290fd9059340954")        # True
print is_integer("42f")        # False

import re

def is_number(string):
    return bool(re.match(r'^-?\d+(?:\.\d{1,2})?$', string))

print is_number("42.01")      # True
print is_number("-42")        # True
print is_number("4.b")        # False
print is_number("42.")        # False