#!/usr/bin/env python3
import subprocess
import re
#import cv2
import os
from ke import cycle

print("Что хотите мой повелитель?")
print('1 - гит рабочий реп все чики пуки сделать')
print("2 - какая рабоч директория (реп)")
print('3 - другой рабочий реп сделать')
print('4 - хочу стать птицей')
print('5 - ссылка на раба')

text=0
def inaki():
    k=False
    while k != True:
        try:
            global text
            text = int(input())
            
            k = True
        except:
            print("пОЖАЛУЙСТА введите другое число повелитель *o*")
            k = False
        finally:
            if k == False:
                continue
            else:
                cycle(text)
                inaki()


inaki()













