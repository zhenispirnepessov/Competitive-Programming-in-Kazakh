"""  
Problem solving series

Date: 03-02-2022
12. Number of words | Сөздер саны - Python Есептер
Бос орындармен бөлінген сөздерден тұратын жол берілген. 
Құрамында қанша сөз барын анықтаңыз. Есепті шешу үшін 
count() әдісін қолданбаңыз.

* * * * * * * * * * * * * *
Test 1:
Енгізілген деректер (Input): 
Hello world
Шығарылган деректер (Output): 
2
* * * * * * * * * * * * * *
Test 2:
Енгізілген деректер (Input): 
Сенің көзің түпсіз терең
Шығарылган деректер (Output): 
4
"""

a = input()

# print(a.count(" ") + 1)

n = 1
for i in range(0, len(a), 1):
    if a[i] == " ":
        n += 1      # n = n + 1

print(n)