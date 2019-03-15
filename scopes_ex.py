x=10 # Global
y=10 # Global
def f1():
    x=20 # enclosed scope. Can be accessed from f2 function if x is not defined there
    def f2():
        # x=30 # local scope
        nonlocal x
        x=300
        print('f2 x = ', x)

        global y
        y = 1000
        print('f2 y = ', y)
    f2()
    print('f1 x = ', x)
f1()
print('Global x = ', x)
print('Global y = ', y)

# built-in scope
print(dir(__builtins__)) # prints built-in class, function, variables


count=0
def create_Acc():
    global count
    count = count + 1

def del_Acc():
    global count
    count = count - 1

def total_acc():
    print('total Accs=', count)


create_Acc()
create_Acc()
del_Acc()
count=100
total_acc()


def Account():
    count=0
    def create_acc():
        nonlocal count
        count = count + 1

    def del_acc():
        nonlocal count
        count = count - 1

    def total_acc():
        print('total Accs = ', count)

    return create_acc, del_acc, total_acc

r1 = Account()
ca,da,tc = Account()
ca()
ca()
da()
tc()

r1[0]()
r1[0]()
r1[1]()
r1[2]()
