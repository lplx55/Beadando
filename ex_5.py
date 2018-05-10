import itertools
from itertools import chain

def tupleToList(lst):
    return list(chain.from_iterable(lst))

signs=['+','-','']
numbers=[i for i in range(1,10)]
options=[]
signlist=[list(p) for p in itertools.product(signs,repeat=8)]
num=0
while num <9:
    for combinations in signlist:
        options=list(zip(numbers,combinations))
        options.append((9,''))
        options=tupleToList(options)
        a = ''.join(str(x) for x in options)
        if eval(a)== 100:
            print(a, '=100')
        num+=1