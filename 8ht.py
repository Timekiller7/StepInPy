#сгенерировать хтмл файл - таблица умножения ,значения в ячейках
#для перехода по ссылкам 
#n=str(list[i][j])
#    with tag('a', href='http://'+n+'.ru'):
#        text(n)

from yattag import Doc

doc, tag, text = Doc().tagtext()
list = [[0] * 10 for i in range(10)]
for i in range(10):
    for j in range(10):
         list[i][j]=(j+1)*(i+1)

with tag('html'):
    text('\n')
    with tag('body'):
        text('\n')
        with tag('table'):
            text('\n')
            for i in range(10):
               with tag('tr'):
                  for j in range(10):
                     with tag('td'):
                       text(str(list[i][j]))
                  text('\n')
               text('\n')
        text('\n')
    text('\n')

result = doc.getvalue()
print(result)
