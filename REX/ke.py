import subprocess
import re
import os
name=""
def edit(text):
    a=3
    a_file = open('/Users/macos/Documents/scripts/robot', "r")
    list_of_lines = a_file.readlines()
    a_file.close()
    if text==3:
        global name
        list_of_lines[1] = "cd /Users/macos/octopus/" + name + '\n'
    if text==1:
        a=int(input("Коммит по дефолту(0) или свой(1)?"))
    if a==1:
        s=input()
        list_of_lines[3]="git commit -am "+' "{}" '.format(s)+"\n"
    a_file = open('/Users/macos/Documents/scripts/robot', "w")
    a_file.writelines(list_of_lines)
    a_file.close()


def cycle(text):
    if (text == 1):
        edit(text)
        subprocess.call("/Users/macos/Documents/scripts/robot")
        default = "roboti zahvatyat mir { nechelovecheskii commit }"
        a_file = open('/Users/macos/Documents/scripts/robot', "r")
        list_of_lines = a_file.readlines()
        a_file.close()
        list_of_lines[3] = "git commit -am " + ' "{}" '.format(default)+"\n"
        a_file = open('/Users/macos/Documents/scripts/robot', "w")
        a_file.writelines(list_of_lines)
        a_file.close()
    if (text == 2):
        f = open('/Users/macos/Documents/scripts/robot', 'r')
        for line in f:
            if line.startswith('cd'):
                print(re.sub(r'cd ', "", line))
                break
        f.close()
    if (text == 3):
        f=os.listdir("/Users/macos/octopus")
        if ".DS_Store" in f:
            f.remove(".DS_Store")
        k=0
        for i in f:
            print(i," - ",k)
            k+=1
        num=int(input("Какую репу хотите сделать рабочей?"))
        global name
        name=f[num]
        edit(text)

    if (text == 4):
        exit()
    if (text == 5):
        print("/Users/macos/Documents/scripts")
        print("Имя слуге - робот")
