from random import *
def arvud_loendis():
    print("Данные:")
    s=[]
    pos=[]
    neg=[]
    nol=[]
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:
        mini,maxi=vahetus(mini,maxi)
    generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    jagamine(s,pos,neg,nol)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",nol)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    print(s)

def vahetus(mini:int,maxi:int):
    '''Меняет местами минимальное значение и максимальное
    :rtype: int,int
    '''
    abi=mini
    mini=maxi
    maxi=abi
    return mini,maxi

def generaator(n:int,s:list,mini:int,maxi:int):
    '''Генерирует списки от минимального числа до максимального
    '''
    for i in range(n):
        s.append(randint(mini,maxi))
    
def jagamine(s:list,pos:list,neg:list,nol:list):
    '''Создает списки с позитивными,негативными и нулевыми числами
    '''
    for el in s:
        if el>0:
            pos.append(el)
        elif el<0:
            neg.append(el)
        else:
            nol(append(el))

def keskmine(s:list,):
    '''Выявляет среднее число
    '''
    n=len(s)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in s:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(s:list,el:float):
    '''Добавляет число в список и сортирует его
    '''
    s.append(el)
    s.sort()