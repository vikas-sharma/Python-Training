#dict -> class


D={'course':'python', 'dur':5, 'loc':'pune'}

print(D['course'])

#print(D['author'])
r1=D.get('author', 'No such key')
print('r1=', r1)

#add & update

D['course']=['java','c']
print('D=', D)

#Remove

E=D.copy()
r1=D.pop('course')
print(D, r1)

del D['dur']
x=10
del x

r2=D.popitem()
print(r2)


k=E.keys()
v=E.values()
i=E.items()

print(k,v,i, sep='\n')
