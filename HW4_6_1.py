# script1

from sys import argv
from itertools import count

filename, x, y = argv

for el in count(int(x)):
    if el > int(y):
        break
    print(el)
