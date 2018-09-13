class element:
    def __init__(self,name,size,align):
        self.name =name
        self.size =size
        self.align=align
        def __setattr__(self,name,value):
            raise AttributeError("This class is read-only.")
        self.__setattr__
    def __str__(self):
        return str((self.name,self.size,self.align))
from functools import reduce
def gcd(*i):
    from math import gcd
    return reduce(gcd,i,0)
def product(*i):
    return reduce(lambda x,y:x*y,i,1)
def lcm(*i):
    return reduce(lambda x,y:x*y//gcd(x,y),i,1)
c=element('c',1,1)#char:  has size 1 and have address divisble by 1
s=element('s',2,2)#short: has size 2 and have address divisble by 2
i=element('i',4,4)#int:   has size 4 and have address divisble by 4
f=element('f',4,4)#float: has size 4 and have address divisble by 4
d=element('d',8,4)#double:has size 8 and have address divisble by 4
def struct(*elements,name=None):
    #Takes multiple elements and returns a single element
    size=0
    align=1
    for e in elements:
        assert isinstance(e,element)
        size+=-size%e.align+e.size#pad with bytes then align e on it's boundary
        align=lcm(align,e.align)#lcm is both commutative and associative
    size+=-size%align#Make this struct able to be packed into arrays by padding it's size to fit it's alignment
    return element(name,size,align)
def optimize(*elements):
    #takes elements and returns the best order of these elements to minimize their size as a struct
    from itertools import permutations
    best =min(permutations(elements),key=lambda x:struct(*x).size)
    worst=max(permutations(elements),key=lambda x:struct(*x).size)
    print("best: " + ' '.join(x.name for x in best )+" at size "+str(struct(*best ).size))
    print("worst:" + ' '.join(x.name for x in worst)+" at size "+str(struct(*worst).size))
#DEMO:
print(optimize(c,s,c))#c c s at size 6
print(optimize(c,i,c))#c c i at size 8
print(optimize(c,s,c,i,c,s,i,c))#c c s i c c s i at size 16
