'''
Файл https://stepik.org/media/attachments/lesson/209719/2.html содержит статью с Википедии про язык Python. В этой статье есть теги code, которыми выделяются конструкции на языке Python. Вам нужно найти все строки, содержащиеся между тегами <code> и </code> и найти те строки, которые встречаются чаще всего и вывести их в алфавитном порядке, разделяя пробелами.

Например, если исходный текст страницы выглядел бы так:

<code>a</code>
<a>bracadabr</a>
<code>c</code>
<code>b</code>
<code>b</code>
<code>c</code>
то в ответ надо было бы ввести строку "b c".


'''
from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
s=str(html)
arr=[]
kol=[0]*1000
first=s.find("<code>")
a=0
while first!=-1:
    sec=s.find("</code>")
    temp = s[first + 6:sec]                               #l=s[first+6:sec+7]
    if temp in arr:
        i = arr.index(temp)
        kol[i]+=1
    else:
        arr.append(temp)
        kol[arr.index(temp)]=1
    s=s[sec+7:]
    first = s.find("<code>")

for i in range(len(kol)-1):
    for j in range(len(kol)-i-1):
        if kol[j] < kol[j+1]:
            kol[j], kol[j+1] = kol[j+1], kol[j]
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)


#######Некоторые примеры
#1
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245130/6.html') # скачиваем файл
html = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') # делаем суп
table = soup.find('table', attrs = {'class' : 'wikitable sortable'})

print(table)



#2 Парс таблицы, вывести сумму элементов

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html') # скачиваем файл
html = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') # делаем суп
sum=0
table = soup.table
table_rows = table.find_all('tr')
for tr in table_rows:
td = tr.find_all('td')
row = [i.text for i in td] 
for i in row:
t=int(i)
sum+=t

print(sum)

//// + ДОП решение

#все тэги внутри td игнорируются,только текст вытягивает типа:
<td><i> 19 </i></td>

import requests as req
from bs4 import BeautifulSoup
res = req.get('https://stepik.org/media/attachments/lesson/209723/3.html')
soup = BeautifulSoup(res.text, 'html.parser')
print(sum(int(td.text) for td in soup.find_all('td')))




#3Типа скачки файла:
import requestsimport xmltodict
url = 'https://stepik.org/media/attachments/lesson/245571/map1.osm'xml = requests.get(url).content

