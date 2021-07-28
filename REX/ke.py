
import subprocess
import re

def edit(text):
    a=3
    if text==3:
        name = input("введите название репапапо")
    a_file = open('/Users/macos/Documents/scripts/robot', "r")
    list_of_lines = a_file.readlines()
    a_file.close()
    if text==3:
        list_of_lines[1] = "cd /Users/macos/octopus/" + name + '\n'
    if text==1:
        a=int(input("Коммит по дефолту(0) или свой(1)?"))
    if a==1:
        s=input()
        list_of_lines[3]="git commit -am "+s
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
        list_of_lines[3] = "git commit -am " + default
        a_file = open('/Users/macos/Documents/scripts/robot', "w")
        a_file.writelines(list_of_lines)
        a_file.close()
    if (text == 2):
        f = open('/Users/macos/Documents/scripts/robot', 'r+')
        for line in f:
            if line.startswith('cd'):
                print(re.sub(r'cd ', "", line))
                break
        f.close()
    if (text == 3):
        edit(text)

        # if (text == 4):
        #  img = cv2.imread('/Users/macos/Downloads/koza.png', 0)
        # cv2.imshow("yporotay ptiza", img)
        # cv2.waitKey(0)                                       #кликнуть на картину и enter
        # cv2.destroyAllWindows()
    if (text == 4):
        exit()
    if (text == 5):
        print("/Users/macos/Documents/scripts")
        print("Имя слуге - робот")
