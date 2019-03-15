F1=open('out1.txt', 'w')

x=10
s='Python\n'
x=str(x) + '\n'

F1.write(x)
F1.write(s)
F1.flush()


L=[x,s]
F1.writelines(L)

F1.close()

F2=open('out1.txt', 'r')

r1=F2.read()
print('r1=',r1)

# seek pointer is at the end now, so set it to 0 otherwise r2 will be empty

F2.seek(0)
r2=F2.read()
print('r2=', r2)

F2.seek(0)
r3=F2.readline()
print('r3=', r3)

F2.seek(0)
while True:
    line=F2.readline()
    if line == '': #EOF
        break
    else:
        print('line = ', line)

F2.seek(0)
r4=F2.readlines()
print('r4=', r4)

r5=[]
for line in r4:
    r5.append(line.strip())
print('r5=', r5)


F2.seek(0)
for line in F2:
    print('line=', line.strip())

F2.close()


F3=open('out1.txt', 'a')
F4=open('out2.csv', 'a')

print(20, 'java', sep='\n', file=F3, flush=True)
print(20, 'java', sep=',', file=F4)

F3.close()
F4.close()

#'w' -> write only
#'r' -> read only
#'a' -> append only
#'w+' -> WR
#'r+' -> RW
#'a+' -> AR