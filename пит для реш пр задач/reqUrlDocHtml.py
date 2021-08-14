''''
Рассмотрим два HTML-документа A и B. Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти за один переход.
Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.
Sample Input 1:
https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample2.html
Sample Output 1:
Yes
'''
import requests
import re
A = input()
B = input()
pattern = r'http.*html'
list_urlA = re.findall(pattern, requests.get(A).text)
list_url = []
for url in list_urlA:
    list_url += re.findall(pattern, requests.get(url).text)
if B in list_url:
    print('Yes')
else:
    print('No')