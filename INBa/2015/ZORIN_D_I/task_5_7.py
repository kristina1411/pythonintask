# Задача 5. Вариант 7.
# Напишите программу, которая бы при запуске случайным образом отображала имя одного из семи гномов, друзей Белоснежки.
#
# Zorin D.I.
#11.04.2016
import random
s = "Имя одного из семи гномов: "
a = random.randint(1,7)
if a == 1:
   print(s+"Умник")
elif a == 2: 
   print(s+"Ворчун")
elif a == 3: 
   print(s+"Весельчак")
elif a == 4: 
   print(s+"Соня ")
elif a == 5: 
   print(s+"Скромник ")
elif a == 6: 
   print(s+"Чихун")
elif a == 7: 
   print(s+"Простачок")
input("Нажмите ENTER для продолжения")
