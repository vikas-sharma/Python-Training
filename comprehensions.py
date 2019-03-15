#Comprehensions

L1=[i for i in range(10)]

L2=[i*i for i in L1 if i%2==0]

T1=(i*i for i in L1 if i%2==0) # Tuple automatically become generator object when writing expression inside it

print('T1=', list(T1))
print('T1=', list(T1))

F=open('out1.txt')
L3=[line.strip() for line in F]

L4=[(lambda i : i*i)(i) for i in L1 if i%2==0]

F2=open(r'C:\vikas\log\server.txt')
ip=[line.split()[0] for line in F2 if line[:3].isdigit()]

k=['k1', 'k2']
v=[10,20]
D={k:v for k,v in zip(k,v)}

E={k:(lambda x:x+10)(v) for k,v in zip(k,v)}