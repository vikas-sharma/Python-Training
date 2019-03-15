import copy

#list -> class

L=[10, 12.5, 'python', ['a', 'b']]
print(L)
print(L[1])
print(L[2][1])

print(L[1:])

#Update
L[1] = 'java'
print('update = ', L)

#add

L.append(200)
print('append = ', L)

L.insert(2, 'C++')
print('insert = ', L)

L1=[10, 20]
L2=['a', 'b']
L3 = L1 + L2
L4 = L1 * 10
print(L3, L4)


L1.extend(L2)

#Remove
r1 = L.pop()

r2 = L.pop(2)

r3=L.remove('python')
print('remove = ', L, r3)

L5=[20,10,30]
L5.sort()

print(L5)

L6=['z','a','x']
L6.sort(reverse=True)

print(L6)

i=L6.index('z')
c=L6.count('z')
print(i, c)


#copy

L7=[10,20,['a','b']]
L8=L7 # Reference copy

L9=L7.copy() #shallow copy
L9[1]=30


L10 = copy.deepcopy(L8) #deep copy

print(id(L8[0]), id(L8[2]))
print(id(L10[0]), id(L10[2]))

#empty

L10.clear()
