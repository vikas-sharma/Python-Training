a=10

if a == 10:
    pass

def add1():
    pass

def add2():
    a=10
    b=20
    c=a+b
    print('c = ', c)

add2()
print ('Some line')
add2()

def add3():
    a=10
    b=20
    c=a+b
#    return c
#    print('add3=', c)
#    return
#    return a,b,c
    return (a+b)/(a-b)

r1=add3()
print('r1=', r1)

# positional arguments

def add4(a, b):
    return a+b

r2=add4(10,20)
print('r2 = ', r2)

# positional args with default values

def add5(a,b=10):
    return a+b

r3=add5(10)
print(r3)
r4=add5(20,30)
print(r4)

# variable args

def add6(a, b=10, *c):  # *c is called packing
    print('Remaining args passed: ', c)
    r=a+b
    for i in c:
        r=r+i
    return r

r5 = add6(10)
print('r5=', r5)

r6 = add6(10,20,30,40)
print('r6=', r6)


# keyword only Args

def add7(a, b=10, *c, d, e):# d and e are keyword only argument
    r = a+b+d+e
    for i in c:
        r = r+ i
    return r


r7 = add7(10,20,30,40,d=50, e=60)

print('r7=', r7)

# variable keyword only args

def add8(a,b=10,*c,d,e,**f):
    print('Remaining keyword only Args: ', f)
    r = a+b+d+e
    for i in c:
        r = r + i
    for j in f.values():
        r = r + j
    return r

r8 = add8(10,20,30,40,d=50,e=60,f=70,g=80)

print('r8 = ', r8)


# unpack

L=[10,20,30,40,50,60]
r9 = add6(*L) # unpack

D={'d':50, 'e':60}
r10 = add7(*L, **D)


# add()
# add(a,b)
# add(a=10,b=10)
# add(*a)
# add(*a, **b)
# add(*,a,b)
# add(**a)