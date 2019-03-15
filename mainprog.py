from project.net import mymodule, mymodule as m
import sys
print(sys.path)

#sys.path.append(r'C:\vikas\lib') # another way to set path. First way to set in Windows'path - PYTHONPATH

print (mymodule.msg)
print(mymodule.add(10, 20))

line='-' * 40
print(line)

print(m.msg)
print(m.add(30,40))

print(line)

from project.net.mymodule import msg, add

print(msg)
print(add(50,60))

print(line)

from project.net.mymodule import msg as m, add as a
print(m)
print(a(70,80))

print(line)

from project.net.mymodule import *

print(msg)
print(add(90,100))

print(line)

import project.net.mymodule

print(project.net.mymodule.msg)
print(project.net.mymodule.add(10,20))

print(line)

import project.net.mymodule as m

print(m.msg)

print(line)

from project.net.mymodule import add, msg

print(msg)
