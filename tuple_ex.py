#tuple -> class


T=(10, 12.5, 'python', ['a', 'b'], (10,20))

print(T)
print(T[1])
print(T[1:])
i=T.index('python')
c=T.count(12.5)

print(i, c)

# convert to List and vice-versa

L=list(T)
print('L=', L)
L.append(20)
T=tuple(L)
print('T=', T)
