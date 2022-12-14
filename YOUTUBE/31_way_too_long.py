"""  
Problem solving series

Date: 05-02-2022
14. Way Too Long Words - short | Өте ұзақ сөздер - Python Есептер

Кейде "localization" немесе "internationalization" сияқты кейбір сөздердің 
ұзақ болатыны сонша, оларды бір мәтінде бірнеше рет жазу әбден жалықтырады.

Егер оның ұзындығы 10 таңбадан асатын болса, сөзді тым ұзын деп қарастырайық. 
Барлық тым ұзын сөздерді арнайы аббревиатурамен ауыстыру керек.

Бұл аббревиатура былай жасалады: сөздің бірінші және соңғы әрпін жазамыз 
және олардың арасына бірінші және соңғы әріптердің арасындағы әріптердің 
санын жазамыз. Бұл сан ондық жүйеде және алдыңғы нөлдерді қамтымайды.

Осылайша, "localization" "l10n" деп жазылады, ал "internationalization" "i18n" 
болып жазылады.

Сізге қысқартылған сөздерді өзгерту процесін автоматтандыру ұсынылады. Бұл 
ретте тым ұзақ сөздер аббревиатурамен ауыстырылуы керек, ал тым ұзын емес 
сөздер ешқандай өзгеріске ұшырамауы керек.

* * * * * * * * * * * * * *
Test 1:
Енгізілген деректер (Input): 
word
Шығарылган деректер (Output): 
word
* * * * * * * * * * * * * *
Test 2:
Енгізілген деректер (Input): 
localization
Шығарылган деректер (Output): 
l10n
* * * * * * * * * * * * * *
"""

a = input()

if len(a) > 10:
    # birinshi_tangba = a[0]
    # songgy_tangba = a[-1]
    # orta_tangbalar_sany = len(a) - 2
    print(a[0] + str(len(a) - 2) + a[-1])
else:
    print(a)