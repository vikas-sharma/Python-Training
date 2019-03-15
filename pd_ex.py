import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('dbdump.csv')
df2=df['IP']
df3=df['ID'].describe()
df4=df['ID'].mean()
df5=df['PICS'].value_counts()

df5.plot()
#plt.show()

df5.plot.bar()
plt.savefig('graph.png')

writer=pd.ExcelWriter('Report.xlsx', engine='xlsxwriter')
df5.to_excel(writer, sheet_name='Data')
wb = writer.book
ws = wb.add_worksheet('graph')
ws.insert_image('B1', 'graph.png')
writer.close()

df6=df[df['ID'] > 10]
df7=df[df['PICS'].str.endswith('jpg')]
df8=df.groupby(['PICS']).count()
df9=df.iloc[1]
df10=df.iloc[1:3]
df11=df.iloc[1:3, 1]
df12=df.iloc[1:3,1:3]
df13=df.iloc[1,2]
df14=df.iloc[[1,3],[2,4]]
print(df14)
