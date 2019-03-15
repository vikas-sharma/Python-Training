from sklearn.neighbors import KNeighborsClassifier as kn
import pandas as pd

def getresult(*a):

    df=pd.read_csv(r'C:\vikas\log\iris.csv')

    # All rows and first 4 columns
    x = df.iloc[:,:4]

    # All rows and extract last column
    y = df.iloc[:, 4]

    #replace string target with numeric target
    y = y.replace('setosa', 0)
    y = y.replace('versicolor', 1)
    y = y.replace('virginica', 2)

    mymodule = kn()

    # training the data. x is feature, y is target
    mymodule.fit(x, y)

    return mymodule.predict([a])

def numToString(res):
    if res == 0:
        return 'type is setosa'
    elif res == 1:
        return 'type is versicolor'
    elif res == 2:
        return 'type is virginica'
    else:
        return 'unknown type'


res = getresult(3,5,4,2)
print(numToString(res))
