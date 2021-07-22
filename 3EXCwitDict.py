'''
Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно,
составив справочник продуктов с указанием калорийности на 100 грамм,
а также содержание белков, жиров и углеводов на 100 грамм продукта.
Ему не удалось найти всю информацию, поэтому некоторые ячейки остались
незаполненными (можно считать их значение равным нулю).
Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx

Вася составил раскладку по продуктам на один день (она на листе "Раскладка")
с указанием названия продукта и его количества в граммах.
Посчитайте 4 числа: суммарную калорийность и граммы белков, жиров и углеводов.
Числа округлите до целых вниз и введите через пробел.
'''

import xlrd
rb = xlrd.open_workbook('trekking2.xlsx')
sh = rb.sheet_by_index(0)
sh2=rb.sheet_by_index(1)
dict={}
cool=0
bel=0
zhir=0
ugl=0
vals = [sh.row_values(rownum) for rownum in range(sh.nrows)][1:]
val2=sh2.col_values(0)[1:]
wei=sh2.col_values(1)[1:]
for i in range(len(vals)):
    if vals[i][0] in val2:
        x = val2.count(vals[i][0])
        temp=val2
        for k in range(len(vals[i])-1):
            if vals[i][k+1]=="":
                vals[i][k + 1]=0
        we = wei[val2.index(vals[i][0])] / 100
        if x == 1:
            dict[vals[i][0]] = [vals[i][1]*we, vals[i][2]*we, vals[i][3]*we, vals[i][4]*we, we*100]
        elif x>1:
            dict[vals[i][0]] = [vals[i][1]*we, vals[i][2]*we, vals[i][3]*we, vals[i][4]*we, we*100]
            while x!=0:
                x=temp[val2.index(vals[i][0])+1] .count(vals[i][0])
                dict[vals[i][0]] [4]+=wei[val2.index(vals[i][0],(val2.index(vals[i][0])+1))]
                for j in range(1,5):
                    if  vals[i][j]!=0:
                        dict[vals[i][0]][j-1]+=float(vals[i][j])*we
        cool+=dict[vals[i][0]][0]
        bel+= dict[vals[i][0]][1]
        zhir += dict[vals[i][0]][2]
        ugl += dict[vals[i][0]][3]
print(int(cool),int(bel),int(zhir),int(ugl))








