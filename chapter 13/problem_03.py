def divisible5(n):
    if(n%5==0):
        return True
    return False
a = [1,4,5,67,43,6,7,88,44]

f= list(filter(divisible5,a))
print(f)
