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
