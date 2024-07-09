import requests
import re
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
#--------------1
labels = []# 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = []# 15, 30, 45, 10
array = []
with open("\\".join([dir_path,"text.txt"])) as file:
    array = [row.strip() for row in file]

a = 0
while a < len(array):
    
#--------------1
    r = requests.get(array[a])
    a=a+1

    pattern = re.compile(r'Количество поступающих:*\d+')
    match = pattern.search(r.text)

    print("-------------------------------------")
    if match:
        number_of_applicants = int(match.group().split(":")[1].strip())
        print("Количество поступающих:",number_of_applicants)  
    else:
        print("Число поступающих не найдено.")
    
#--------------2

    pattern = re.compile(r'Конкурсная группа: (.*?)<')
    match = pattern.search(r.text)

    if match:
        name = str(match.group().split(":")[1].strip())
        print(name)
    else:
        print("Название конкурсной группы не найдено.")
    labels.append(name)
    sizes.append(number_of_applicants)

#-------------2

import matplotlib.pyplot as plt

fig1, ax1 = plt.subplots(figsize=(15,10))

#print(labels)
#print(sizes)

ax1.set_title('График количества поступающих абитуриентов')
plt.matplotlib.pyplot.subplots_adjust(left=0.300, bottom=None, right=None, top=None, wspace=None, hspace=None)
plt.xlabel('labels', fontsize=1)
plt.ylabel('size', fontsize=1)


ax1.barh(labels, sizes)

plt.savefig('barh.png')
plt.show()
