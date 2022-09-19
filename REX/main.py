#!/usr/bin/env python3
from ke import cycle

print("Что хотите сделать?")
print('1 - add + commit + push')
print("2 - какая рабочий репозиторий используется роботом?")
print('3 - установить другой рабочий репозиторий')
print('4 - выйти из программы')
print('5 - ссылка на работника')

text=0
def inaki():
    k=False
    while k != True:
        try:
            global text
            text = int(input())
           
            k = True
        except:
            print("введите другое число")
            k = False
        finally:
            if k == False:
                continue
            else:
                cycle(text)
                inaki()


inaki()













