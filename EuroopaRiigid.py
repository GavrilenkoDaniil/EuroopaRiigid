from module1 import *
f=open('riigid.txt' , 'r')
riigid={}
riigid1={}
riig=[]
linn=[]
for line in f:
    k, v=line.strip().split('-')
    riigid[k.strip()] = v.strip()
    riigid1[v.strip()] = k.strip()
    riig.append(k)
    linn.append(riigid[k.strip()])
z=''
while True:
    z=int(input('1 - Ввод страны и показ его столицы\n2 - Тест'))
    if z==1:
        poisk(riigid,riigid1)
    elif z==2:
        test(riigid,riig)
    else:
        print('Выбери 1 или 2')
        break