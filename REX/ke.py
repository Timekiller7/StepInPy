
import subprocess
import re
def cycle(text):
    if (text == 1):
        subprocess.call("/Users/macos/Documents/scripts/robot")
    if (text == 2):
        f = open('/Users/macos/Documents/scripts/robot', 'r+')
        for line in f:
            if line.startswith('cd'):
                print(re.sub(r'cd ', "", line))
                break
        f.close()
    if (text == 3):
        name = input("введите название репапапо")
        a_file = open('/Users/macos/Documents/scripts/robot', "r")
        list_of_lines = a_file.readlines()
        list_of_lines[1] = "cd /Users/macos/octopus/" + name + '\n'

        a_file = open('/Users/macos/Documents/scripts/robot', "w")
        a_file.writelines(list_of_lines)
        a_file.close()

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
