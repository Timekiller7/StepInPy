'''
В OpenStreetMap XML встречаются теги node, которые соответствуют некоторым точкам на карте.
Ноды могут не только обозначать какой-то точечный объект, но и входить в состав way
(некоторой линии, возможно замкнутой) и не иметь собственных тегов.
Для доступного по ссылке https://stepik.org/media/attachments/lesson/245678/map1.osm фрагмента карты
посчитайте, сколько node имеет хотя бы один вложенный тэг tag,
а сколько - не имеют. В качестве ответа введите два числа, разделённых пробелом.
'''
import requests
import xmltodict
url = 'https://stepik.org/media/attachments/lesson/245571/map1.osm'
xml = requests.get(url).content
ex=0
unex=0
dc = xmltodict.parse(xml)
for node in dc['osm']['node']:  #в тэге осм все ноды - чистый словарь а в нодах все атрибуты объектов
    if 'tag' in node:
        ex+=1
    else:
        unex+=1

print(ex,unex)
print(dc['osm'])


#1
Типа скачки файла:
import requestsimport xmltodict
url = 'https://stepik.org/media/attachments/lesson/245571/map1.osm'xml = requests.get(url).content

#2 из xml в словарь
import xmltodict

fin=open('map1.osm','r',encoding='utf8')
xml=fin.read()
fin.close()
parsedxml=xmltodict.parse(xml)
print(parsedxml['osm']['node'][100]['@id'])

