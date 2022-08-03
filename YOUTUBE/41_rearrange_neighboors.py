"""  
Problem solving series

Date: 19-02-2022
19. Көрші элементтерді орнын ауыстыру | Replace adjacent elements 
sign - Python Есептер

Массивтің көршілес элементтерін ауыстыратын программа жазыңыз 
(1-ші элементті 2-мен, 3-ші элементті 4-ші элементпен өзгерту және т.б. 
Элементтердің саны тақ болса, онда соңғы элемент өз орнында қалады).
* * * * * * * * * * * * * *
Test 1:
Енгізілген деректер (Input): 
5
1 2 3 4 5
Шығарылган деректер (Output): 
2 1 4 3 5
* * * * * * * * * * * * * *
Test 2:
Енгізілген деректер (Input): 
6
4 5 3 4 2 3
Шығарылган деректер (Output): 
5 4 4 3 3 2 
* * * * * * * * * * * * * *
"""
n = int(input())
l = list(map(int, input().split()))[:n]

for i in range(1, n, 2):
    l[i-1], l[i] = l[i], l[i-1]     # a, b = b, a

print(*l)