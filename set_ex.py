#Set -> class

#unordered
#no index
#no key
#sets and union
#unique values

S={10,10,'python','python'}
print(S)

S.add(20)
S.add(20)
print(S)


t=S.copy()
r1=S.remove('python')
r2=S.pop()

print(S, r1, r2)



L=[]
print(dir(L)) # tell all the method in the class

print(help(L.append))
