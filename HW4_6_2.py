# script2

from sys import argv
from itertools import cycle

filename, finish = argv
i = 1

zen = ['Beautiful', 'is', 'better', 'than', 'ugly.']

for el in cycle(zen):
    if i > int(finish):
        break
    print(el)
    i += 1
