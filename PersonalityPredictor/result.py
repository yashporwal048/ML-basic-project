import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import csv
def predict():
    data =pd.read_csv('train dataset.csv')
    array = data.values
    for i in range(len(array)):
        if(array[i][0]=="Male"):
            array[i][0]=1
        else:
            array[i][0]=0
    df=pd.DataFrame(array)
    maindf =df[[0,1,2,3,4,5]]
    mainarray=maindf.values
    
    temp=df[6]

    train_y =temp.values
    #print(train_y)

    train_y=temp.values

    for i in range(len(train_y)):
        train_y[i] =str(train_y[i])
    
    mul_lr =DecisionTreeClassifier()
    mul_lr.fit(mainarray, train_y)
    
    e=n=c=o=a=0
    File = open('responce.csv')
    Reader=csv.reader(File)
    Data=list(Reader)
    #print(Data)
    print(len(Data))
    Data1= [x for x in Data if x != []]
    for i in range (8):
        e=e+float(Data1[i][1]) #first list ka first element and so on
    er=round(e)
    print(er)
    for i in range (8,16):
        a=a+float(Data1[i][1]) #first list ka first element and so on
    ar=round(a)
    print(ar)
    for i in range (16,24):
        c=c+float(Data1[i][1]) #first list ka first element and so on
    cr=round(c)
    print(cr)
    for i in range (24,32):
        o=o+float(Data1[i][1]) #first list ka first element and so on
    oro=round(o)
    print(oro)
    for i in range (32,40):
        n=n+float(Data1[i][1]) #first list ka first element and so on
    nr=round(n)
    print(nr)
    File.close()
    y_pred = mul_lr.predict([[0,oro,nr,cr,ar,er]])
    print(y_pred)

    return '<h1>{{y_pred}}</h1>'