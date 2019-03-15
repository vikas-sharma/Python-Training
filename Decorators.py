def add(a,b):
    print('Result is:')
    print(a+b)
    print('End of the Res')

def sub(a,b):
    print('Result is:')
    print(a-b)
    print('End of the Res')

add(10,20)
sub(10,20)

# decorated function below

def my_dec(func_to_be_decorated):
    def decorated_func(a,b):
        print('Result is:')
        func_to_be_decorated(a,b)
        print('End of Res:')

    return decorated_func

@my_dec
def add1(a,b):
    print(a+b)
@my_dec
def sub1(a,b):
    print(a-b)

add1(30,40)
sub1(30,40)

def add2(a,b):
    print(a+b)

f = my_dec(add2)
f(100,200)