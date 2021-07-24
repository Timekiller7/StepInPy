#из многих Эксель файлов вытянуть строчки и в текст файл закинуть
import xlrd
import os
import collections
cwd = os.path.abspath('')
files = os.listdir(cwd)
dict={}
ans = open('answer.txt', 'w', encoding='utf-8')
for file in files:
     if file.endswith('.xlsx') or file.endswith('lsx',) :
          rb = xlrd.open_workbook(file)
          sh = rb.sheet_by_index(0)
          row = sh.row_values(1)[1:]
          dict[row[0]]=int(row[2])
     rb.release_resources()
od = collections.OrderedDict(sorted(dict.items()))              #отсортированный словарь - удобно, od запоминает в каком порядке insert элементов был
for k, v in od.items():
     st=str(k)+" "+str(v)+"\n"
     ans.write(st)
