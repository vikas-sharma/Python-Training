#Generators

L=[1,2,3,4]
def squares(M):
    res=[]
    for i in M:
        res.append(i*i)
    return res

r1=squares(L)
for j in r1:
    print('j=', j)

# Generators yield

def gen_squares(M):
    for i in M:
        yield i*i
    for j in M:
        yield j+j

r2=gen_squares(L) # r2 is generator object
for k in r2:
    print('k=', k)
print('Now r1 & r2=', r1, list(r2))