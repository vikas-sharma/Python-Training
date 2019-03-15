a=10
#b=0
c=10
d=0
try:
    r=a/b
    print('r=', r)
except ZeroDivisionError:
    print('ZDE')
except NameError:
    print('NE')
except:
    print('some error')

try:
    r1=c/d
    r2=a/b
except:
    print('some error')
else:
    print('In else')

e=10
try:
    r=a/e
finally:
    print('in finally')

try:
    r=a/f
except Exception as e:
    print(e)
    print(type(e))


try:
    if d == 0:
        raise ZeroDivisionError
    r=c/d
except:
    print('from raise')


result = 'Test Failed'
try:
    assert 'success' in result, 'testcase got failed'
    print('Test completed successfully')
except AssertionError as a:
    print('a=',a)


class MyError(Exception):
    def __init__(self, m):
        self.msg = m

    def __str__(self):
        return 'Details:' + self.msg

x=0
try:
    if x == 0:
        raise MyError('x is zero')
except MyError as m:
    print('m=', m)