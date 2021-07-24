#!/usr/bin/env python3
import subprocess
import cv2

print("Что хотите мой повелитель?")
print('1 - гит рабочий реп все чики пуки сделать')
print("2 - перейти в рабочую директорию")
print('3 - другой рабочий реп сделать')
print('4 - хочу стать птицей')
print('5-выход')
print('6 - ссылка на раба')
k=False
while k!=True:
    try:
        text=int(input())
        k=True
    except:
        print("пОЖАЛУЙСТА введите другое число повелитель *o*")
        k=False
    finally:
        if k==False:continue
        else: break

if(text==1):
     subprocess.call("/Users/macos/Documents/scripts/robot")
if(text==2):
    print("пока не работает :( ")
if(text==3):
    name=input("введите название репапапо")
    f = open('/Users/macos/Documents/scripts/robot', 'r+')
    for line in f:
        if line.startswith('cd'):
            line='cd /Users/macos/octopus/' +name
    f.close()
if (text == 4):
    img = cv2.imread('/Users/macos/Downloads/koza.png', 0)


    cv2.imshow("yporotay ptiza", img)
    cv2.waitKey(0)                                       #кликнуть на картину и enter
    cv2.destroyAllWindows()

if(text==5):
    exit()
if(text==6):
    print("/Users/macos/Documents/scripts")
    print("Имя слуге - робот")






