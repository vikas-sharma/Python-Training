
a=0

while a < 10:
 print('a=', a)
 a += 1

S='python'
i = 0
while i < len(S):
    print(S[i])
    i += 1

L=[10,20,30]

while L:
    x=L.pop()
    print('processed:', x)

L=['l1','l2','TS','R1','l1', 'TS','R2','l1']

i=0
while i < len(L):
    if L[i].startswith('TS'):
        i += 1
        print(L[i])
        i += 1
    else:
        i += 1

# while else
k=0
while k < len(L):
    if L[k].startswith('R'):
        print('R found')
        break
    else:
        k += 1
else:
    print('not found')

# continue

n=0
while n < len(L):
    if not L[n].startswith('R'):
        n += 1
        continue

    print(L[n])
    n += 1
    print('End of while')

# customize do-while as we don't have do-while loop

cart=[]
while True:
    i=input('Enter item:')
    cart.append(i)
    ch=input('Quit (y/n)?:')
    if ch == 'y':
        print('cart is:', cart)
        break