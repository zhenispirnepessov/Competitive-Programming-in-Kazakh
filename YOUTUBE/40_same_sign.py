"""  
Problem solving series

Date: 18-02-2022
18. Бірдей таңбасы бар екі элемент | Two elements with the same 
sign - Python Есептер

Бүтін сандар массиві берілген. Массивте таңбалары бірдей көршілес 
элементтер жұбының бар-жоғын анықтайтын программа жазыңыз. 
Таңбалары бірдей көрші элементтер жұбы болса, ИӘ сөзін шығарыңыз. 
Әйтпесе, ЖОҚ сөзін шығарыңыз.
* * * * * * * * * * * * * *
Test 1:
Енгізілген деректер (Input): 
5
1 -3 4 -2 1
Шығарылган деректер (Output): 
ЖОҚ
* * * * * * * * * * * * * *
Test 2:
Енгізілген деректер (Input): 
4
9 -1 5 7
Шығарылган деректер (Output): 
ИӘ
* * * * * * * * * * * * * *
"""
n = int(input())    # length of a list
a = list(map(int, input().split()))[:n]

result = "ЖОҚ"
for i in range(n-1):
    if a[i] * a[i+1] > 0:
        result = "ИӘ"
    else:
        result = result

print(result)