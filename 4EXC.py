'''
Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно,
составив справочник продуктов с указанием калорийности на 100 грамм, а также содержание белков,
жиров и углеводов на 100 грамм продукта. Ему не удалось найти всю информацию,
поэтому некоторые ячейки остались незаполненными
(можно считать их значение равным нулю).
Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking3.xlsx

Вася составил раскладку по продуктам на весь поход (она на листе "Раскладка") с указанием
номера дня, названия продукта и его количества в граммах.
Для каждого дня посчитайте 4 числа: суммарную калорийность и граммы белков, жиров и углеводов.
Числа округлите до целых вниз и введите через пробел.
Информация о каждом дне должна выводиться в отдельной строке.
'''

import xlrd
rb = xlrd.open_workbook('trekking3.xlsx')
sh = rb.sheet_by_index(0)
sh2=rb.sheet_by_index(1)
days = [ [0]*4 for i in range(20) ]
wei=sh2.col_values(2)[1:]
dict={}

vals = [sh.row_values(rownum) for rownum in range(sh.nrows)][1:]
vals2= [sh2.row_values(rownum) for rownum in range(sh2.nrows)][1:]

for i in vals:
    if i[1]=="":
        i[1]=0
    if i[2] == "":
        i[2] = 0
    if i[3]=="":
        i[3]=0
    if i[4]=="":
        i[4]=0
    dict[i[0]]=[i[1],i[2],i[3],i[4],0]

for i in range(1, 100):
    temp = sh2.row_values(i)
    we=temp[2]/100
    days[int(temp[0])][0] += dict[temp[1]][0]*we
    days[int(temp[0])][1] += dict[temp[1]][1]*we
    days[int(temp[0])][2] += dict[temp[1]][2]*we
    days[int(temp[0])][3] += dict[temp[1]][3]*we

for i in range(len(days)):
    if days[i][0]==0:
        continue
    print(int(days[i][0]),int(days[i][1]),int(days[i][2]),int(days[i][3]))

