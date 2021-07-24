'''
Вася решил открыть АЗС (заправку).
Чтобы оценить уровень конкуренции он хочет изучить количество заправок в интересующем его районе.
Вася скачал интересующий его кусок карты OSM https://stepik.org/media/attachments/lesson/245681/map2.osm
и хочет посчитать, сколько на нём отмечено точечных объектов (node), являющихся заправкой.
В качестве ответа вам необходимо вывести одно число - количество АЗС.

"Как обозначается заправка в OpenStreetMap" - пример хорошего запроса чтобы узнать,
как обозначается заправка в OpenStreetMap.
'''
import requests
import xmltodict
url = ' https://stepik.org/media/attachments/lesson/245681/map2.osm'
xml = requests.get(url).content
shops=0
k=0
dc = xmltodict.parse(xml)
for node in dc['osm']['node']:  #в тэге осм все ноды - чистый словарь а в нодах все атрибуты объектов
    if 'tag' in node:
        tags = node['tag']
        flag = False
        name = 'noname'
        if isinstance(tags, list):
            for tag in tags:
                if '@k' in tag and tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
                    shops += 1
        else:
            if  tags['@v'] == 'fuel':
                k += 1
            #print("DOP",tags)
print(k)
print(shops)

'''
Есть заправка которая находится не в списке, а в словаре.
elif isinstance(tags,dict):
    if (tags['@v'])=='fuel':
Если в ноде несколько tag, то формируется список, если tag один, то не формируется. 




Вася, открывший заправку в прошлом уроке, разорился. Конкуренция оказалась слишком большой. Вася предполагает, что это произошло от того, что теги заправки могут быть не только на точке, но и на каком-то контуре. Определите, сколько заправок на самом деле (не только обозначенных точкой) есть на фрагменте карты



1 вар: все тож самое + поиск по for node in dc['osm']['way']:
    if 'tag' in node:  ...
2 вар: 
import xmltodict
fin = open('map2.osm', 'r', encoding='utf8')
text= fin.read()
fin.close()
count=0
dct = xmltodict.parse(text)
count=text.count('''v="fuel"''')
print(count)
'''