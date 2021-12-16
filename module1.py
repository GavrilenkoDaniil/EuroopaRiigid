from random import *
def poisk(riigid:dict,riigid1:dict):
    a=input('Какой страны столицу вы хотите узнать?')
    if a not in riigid:
        b=input('Такой страны нет в словаре. Хотите ввести ее?\n1-Да\n2-Нет')
        if b==1:
            c=input('Введите страну: ')
            d=input('Введите столицу данной страны: ')
            riigid.update({c:d})
    else:
        print(riigid[a])
    a=input('Какую страну вы хотите узнать по столице?')
    if a not in riigid1:
        b=input('Такой столицы нет в словаре. Хотите ввести ее?\n1-Да\n2-Нет')
        if b==1:
            c=input('Введите столицу: ')
            d=input('Введите страну: ')
            riigid1.update({c:d})
    else:
        print(riigid[a])

def test(riigid:dict,riig:list):
    h=int(input('Сколько вопросов хотите в тесте?'))
    b=0
    for i in range(h):
        n=randint(0,49)
        a=riig[n]
        p=riigid[riig[n]]
        k=input(f'Введите столицу данного гос-ва,{a},{n}')
        if k!=p:
            print('Неправильно!')
        else:
            print('Правильно!')
            b+1
    o=b/h*100
    print(f'У вас {o} процентов!')#    