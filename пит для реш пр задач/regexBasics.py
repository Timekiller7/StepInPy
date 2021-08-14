#Вам дана последовательность строк.
#Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
import sys,re
l=[]
pattern = r'.*cat.*cat.*'
for line in sys.stdin:
    line = line.rstrip()
    s=re.match(pattern, line)
    if s:
        l.append(s.group())
for i in l:
    print(i)

'''
+++++
 r'.*\\.*'   -бекслэш находит
 .{2} -только два любых символа
.*  - различные символы ноль или несколько раз
#pattern = r'.*\bcat\b.*'      -  содержащие "cat" в качестве слова

+++++
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор)
    pattern = r'.*\b(\w+)\1\b.*' 

+++++ 
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".
Sample Input:
There’ll be no more "Aaaaaaaaaaaaaaa"
AaAaAaA AaAaAaA
Sample Output:
There’ll be no more "argh"
argh AaAaAaA
    pattern = r'\b((a|A)+)\b'
         s=re.sub(pattern, r'argh',line,count=1)

+++++
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w.
Sample Input:
this is a text
"this' !is. ?n1ce,
Sample Output:
htis si a etxt
"htis' !si. ?1nce,
---
pattern = r'.*\b(\w\w+)\b.*'
for line in sys.stdin:
    line = line.rstrip()
    s=re.match(pattern,line)
    if s:
        l.append(s.group())
for i in l:
    pattern = r'(\w)(\w)(\w*)'       #3 группировки с индексами 1,2,3.
    print(re.sub(pattern, r'\2\1\3', i))      #меняем индексы

+++++
# В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
# Буквой считается символ из группы \w
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    fixed = re.sub(r"(\w)(\1)+", r"\1", line) #re.sub(r"(\w)\1+", r"\1", line)
    print(fixed)
    
    
'''