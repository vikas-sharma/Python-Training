F1=open(r'C:\vikas\log\server.txt')
F2=open('out3.txt','w')
F3=open('out4.csv','w')

F2.writelines(['IP\t', 'date\t', 'pics\t', 'Website\n'])

print('IP', 'DATE', 'PICS', 'WEBSITE', sep=',', file=F3)

for line in F1:
    if line[:3].isdigit():
        sp=line.split()
        ip=sp[0]

        dt1=sp[3]
        dt1=dt1.split(':')
        dt1=dt1[0]

        dt2=dt1.lstrip('[')
        dt3=dt1[1:]
        dt4=dt1.replace('[', '')
        dt5=dt1.split('[')[-1]

        dt6=sp[3]
        dt6=dt6[dt6.index('[')+1 : dt6.index(':')]


        #if sp[6].startswith('/pics'):
        #if 'pics' in sp[6]:
        if sp[6][:5] == '/pics':
            im = sp[6] # /pics/abc.jpg
            im1 = im.split('/')
            im1 = im1[-1]
        else:
            im1='no image'

        print(ip, dt6, im1)

        wb=sp[10]
        wb1 = wb.strip('"')
        wb2=wb[1 : -1]
        r=ip + '\t' + dt6 + '\t' + im1 + '\t' + wb2 + '\n'

        F2.write(r)

        print(ip, dt6, im1, wb2, sep=',', file=F3)
