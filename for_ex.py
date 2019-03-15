S='python'

for a in S:
 print('a = ', a)

L=[10,20,30]
b='java'

for b in L:
 print('b=', b)

print('Now a & b = ', a, b)

D={'A':10, 'B':20}
for k in D: # D.keys
 print('k=', k, 'V=', D[k])


for v in D.values():
 print('v=', v)

for i in D.items():
 print(i, i[0], i[1])


for i, j in D.items():
 print(i, j)


L1=[10,20,30]
L2=['a','b']

r1=zip(L1,L2)
print(list(r1))

for i,j in zip(L1,L2):
 print(i,j)

comp=['IBM', 'SYN1', 'SAP', 'SYN2']

for i in comp:
 if i.startswith('SYN'):
  print('found')
  break
else: # only if for loop runs
 print('not found')


for j in comp:
 if not j.startswith('SYN'):
  continue
 if j.startswith('SYN'):
  print('some logic')
 print('End of For')

r1=range(10)
r2=range(1,10)
r3=range(1,10,2)
r4=range(10,1,-2)
print(list(r1), list(r2), list(r3), list(r4), sep='\n')

for i in range(2, 10, 2):
 print(i)