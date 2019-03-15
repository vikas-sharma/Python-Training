import numpy as np
import matplotlib.pyplot as plt

a1=np.array([[10,20,30],[40,50,60]])
print(a1)
print(a1[0])
print(a1[0,1])
print(a1[:,1])

print(a1.size)
print(a1.shape)
print(a1.T)
print(len(a1))

a2=a1+10
print('a2=', a2)

a3=a1+a1
a4=np.append(a1,[70,80,90])
print('a4=',a4)

a5=a4.reshape(3,3)
print('a5=', a5)

a6=np.concatenate([a1,a1], axis=0) # vertical
print('a6=', a6)
a7=np.concatenate([a1,a1], axis=1) # horizontal
print('a7=', a7)

a8=a1[a1>20]
print('a8=', a8)

a9=a1.mean()
print('a9=', a9)

a10=a1.mean(axis=0)
print('a10=', a10)

a11=np.array([10,20,30,40])
a12=np.array([20,40,50])
a13=np.isin(a11,a12)
print('a13=', a13)

a14=a11[a13]
print('a14=', a14)

a15=np.random.random()
print('a15=', a15)

a16=np.random.randint(low=2,high=20,size=10)
print('a16=', a16)

a17=np.arange(1,10,0.5)
print('a17=', a17)

plt.plot(a1)
#plt.show()

rtg = np.loadtxt('ratings.csv', delimiter=',', skiprows=1, dtype=np.str)
print('rtg=', rtg)

F=open('out7.txt', 'w')
users=rtg[:,0]
users=np.unique(users)
users=np.array(users, dtype=np.int32)
#np.savetxt(F, users)
print(*users, file=F)


mid=rtg[:,1]
mid=np.unique(mid)
print('mid=', mid)
mvs=np.loadtxt('movies.csv', delimiter=',', skiprows=1, dtype=np.str, encoding='utf8')
mvsid=mvs[:,0]
r = np.isin(mvsid, mid)
print('r=', r)

m = mvs[:,1][r]
print(m)