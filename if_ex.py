a=10
if a == 10:
 print('a eq 10')
elif a > 10:
 print('a gt 10')
elif a < 10:
 print('a lt 10')
else:
 print('in else')


S='python'

if not S.startswith('java'):
 print('Not Java')

if (S != 'C'):
 print('Not C')

if 'th' in S:
 print('Substring found')


L1=[10,20]
L2=L1
L3=L1.copy()

if 20 in L1:
 print('20 found')

if L1 is L2: # Reference Equality
 print('Both refers same object')

if L1 == L3: # Object equality
 print('contents are same')


D={'A':10, 'B':20}

if 'B' in D: #D.keys()
 print('key B found')

if 20 in D.values():
 print('value 20 found')

if ('B', 20) in D.items():
 print('Item found')
