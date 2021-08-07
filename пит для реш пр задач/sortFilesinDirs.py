import os

f=open('t.txt', 'w')
fil=[]
folder=[]
rootdir = '/Users/macos/PycharmProjects/edu/main'
s=rootdir.find('main')
print(s)
for i in os.walk(rootdir):
    folder.append(i)
for address, dirs, files in folder:
    for file in files:
        if address[33:] not in fil:
           if file.endswith(".py"):
             #  f.write(address+'/'+file+'\n')
                fil.append(address[33:])
fil.sort()
for i in fil:
    f.write(i+'\n')
f.close()


'''
Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, 
и затем найти в данной в файловой структуре все директории, 
в которых есть хотя бы один файл с расширением ".py". 

Ответом на данную задачу будет являться файл со списком таких директорий, 
отсортированных в лексикографическом порядке.

list = os.listdir('/Users/macos/PycharmProjects/edu/main') # dir is your directory path
number_files = len(list)
for i in list:
    if i.endswith(".py"):
        files.append(i)

print(list[0:3])
print( number_files)
'''