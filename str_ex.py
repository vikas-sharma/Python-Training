#Str -> class

a='PERSON'
b="PERSON'S"
c='''PERSON'S HEIGHT XYZ" '''
d="""PERSON"""

e='''line1
line2'''
f='line1\
line2'
g='PERSON\'S'
h='C:\\newfolder\\test\\test.py'
i=r'C:\newfolder\test\test.py' # r means raw string

j='WEL COME'

print(len(j))
print(j[1])

#Slicing
print(j[2:6]) # 2 - inclusive, 6 - exclusive
print(j[:6])
print(j[1:])
print(j[:])

#Step
print(j[1:6:1])
print(j[1:6:2]) # using positive index
print(j[::-1])
print(j[6:1:-2])
print(j[-2:-7:2]) # using negative index
print(j[-1]) #prints last char
print(j[-4:]) #prints last 4 chars

r1=j.startswith('WEL')
print(r1)
r2=j.endswith('COME')
print(r2)
r3=j.isupper()
print(r3)
r4=j.islower()
print(r4)
r5=j.upper()
print(r5)
r6=j.lower()
print(r6)
r7=j.istitle()
print(r7)
r8=j.title()
print(r8)

k='abc'
r9=k.isalpha()
print(r9)

l='123'
r10=l.isdigit()
print(r10)

m='abc123'
r11=m.isalnum()
print(r11)


r12=m[-3].isdigit() #check last 3 characters are numeric
print(r12)

r13=j.replace('E', 'e')
print(r13)

r14=j.index('E') # if not found give error
print(r14)

r15=j.find('E') # if not found, return -1
print(r15)

r16=j.index('E', 3)
print(r16)

r17=j.index('E', 3, 8)
print(r17)

#Concatenation and repetition

s1='Hello'
s2='py'

r18=s1+s2
print(r18)

r19=s1*10
print(r19)

line='-'*40
print(line)

#strip

n='    wel come  '
r20=n.strip()
print(r20)
r21=n.lstrip()
print(r21)
r22=n.rstrip()
print(r22)

p='[Wel[come][]'
r23=p.strip('][eW')
print(r23)
r24=p.lstrip('W[')
print(r24)
r25=p.rstrip('][e')
print(r25)

r26=j.count('E')
print(r26)

#format

x=10
y=20
z=x+y
r27='add of x & y is z'
r28='add of {} & {} is {}'.format(x, y, z)
print(r28)

r29='add of {1} & {2} is {0}'.format(z, x, y)
print(r29)

r30=f'add of {x} & {y} is {z}'
print(r30)

#split

r31=j.split()
print(r31)

r32=j.split('E')
print(r32)

#join

r33='XYZ'.join(r32)
print(r33)

