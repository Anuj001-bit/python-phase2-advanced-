from functools import reduce
a = [1,4,5,67,43,6,7,88,44]

def greater(a,b):
    if(a>b):
        return a 
    return b
print(reduce(greater,a))