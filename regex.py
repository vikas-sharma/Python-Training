import sqlite3

con=sqlite3.connect('mydb.sqlite3')

#import otherdb
#con = otherdb.connect(user='', password='', host='', port='', database='')

cur=con.cursor()
q='''CREATE TABLE IF NOT EXISTS LOGDATA(
    IP VARCHAR(100),
    DATE VARCHAR(100),
    PICS VARCHAR(100),
    WEBSITE VARCHAR(100)
) '''

cur.execute(q)


import urllib.request as u
import re # regular expression module

url='https://www.jafsoft.com/searchengines/log_sample.html'
F=u.urlopen(url)

#    ip -> \d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3} -- 123.123.123.123
#    \d{1,2}/[a-zA-Z]{3}/\d{4} -- 20/Apr/2000

for line in F:
    line = line.decode() # convert byte data to str

    # brackets () are used for grouping. Whichever we want, group them with brackets.
    m = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*?(\d{1,2}/[a-zA-Z]{3}/\d{4}).*GET\s+/(pics/(\w+\.\w+))?.*http[s]?://([a-zA-Z0-9.]+).*', line)

    if m != None:
        ip = m.group(1)
        dt = m.group(2)
        im = m.group(4)
        if im == None:
            im = 'No image'
        wb = m.group(5)

        q=f"INSERT INTO LOGDATA VALUES('{ip}','{dt}','{im}','{wb}')"
        cur.execute(q)
con.commit()

q='SELECT * from LOGDATA'
cur.execute(q)
result=cur.fetchall()
print(result)

import csv

F=open('dbdump.csv', 'w', newline='')
wt=csv.writer(F)
h=['IP', 'DATE', 'PICS', 'WEBSITE']
wt.writerow(h)
for row in result:
    wt.writerow(row)

F.close()

import pandas as pd # for huge data


L=[[10,20,30], [40,50,60]]
print(L)
df1 = pd.DataFrame([[10,20,30], [40,50,60]])
print(df1)
df2 = pd.DataFrame(result)
df2.to_csv('out5.csv', header=None)
df2.to_excel('out6.xlsx')
df2.to_json('out7.json')