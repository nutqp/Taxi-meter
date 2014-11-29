from math import *
''' taxi '''
def taxi(kilometre, minute):
    ''' return '''
    if kilometre <= 1:
        price = 35
    elif kilometre <= 12:
        price = 35 + (kilometre-1)*5
    elif kilometre <= 20:
        price = 90 + (kilometre-12)*5.5
    elif kilometre <= 40:
        price = 134 + (kilometre-20)*6
    elif kilometre <= 60:
        price = 254 + (kilometre-40)*6.5
    elif kilometre <= 80:
        price = 384 + (kilometre-60)*7.5
    else:
        price = 534 + (kilometre-80)*8.5
    ''' price '''
    price = int(price)
    ''' price time '''
    minute1 = (int(floor((minute*1.50)/2))*2)-1
    ''' sum price + time '''
    summ = price + minute1
    print price,summ
taxi(input(), input())
