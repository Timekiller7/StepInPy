import csv
with open('Crimes.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')  #[5] - type of the crime, [2] - year
    dict={}
    flag=True
    for row in spamreader:
        if flag:
            flag=False
            continue
        s=row[2].split(" ")
        s=s[0][-4:]
        if s=='2015':
            try:
                 dict[row[5]]+=1
            except:
                dict[row[5]]=0
    type=""
    max=0;
    for key,value in dict.items():           #оч полезная штука
        if not flag:                                 #dict_items([('NARCOTICS', 253), ('BATTERY', 472)...
            type=key                             #еще есть .values
            max=value
            flag=True
            continue
       # print(key,value)        NARCOTICS 253
        if max<value:
            max=value
            type=key
    print(type,max)