#map

L=[100,200,300,400]

def disc(p):
    return p - 10

r1=map(disc, L) # map is implementing generator.

print(list(r1)) # r1 is referring to generator object. Once list is run, generator will execute
print(list(r1)) # generator has executed. So, second time, it won't generate list.

#filter

def filt(p):
    return p > 100 and p < 400

r2=filter(filt, L)

print(list(r2))
print(list(r2))

#reduce (not built in)
from functools import reduce

def red(p,q):
    return p+q

r3 = reduce(red, L)
M=['W','E', 'L']

r4=reduce(red, M)
print(r3, r4)

#lambda

r5 = map(lambda P : P - 10, L)
print(list(r5))

r6 = filter(lambda P : P > 100 and P < 400, L)
print(list(r6))

r7 = reduce(lambda p,q : p+q, L)
print(r7)

add = lambda a,b : a+b # lambda function assigned to variable add. Function name is now add
r8 = add(10, 20)
print(r8)

L = [lambda a,b : a+b] # lambda inside a list
r9=L[0](10,20)