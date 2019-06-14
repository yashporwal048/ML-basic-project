import csv
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