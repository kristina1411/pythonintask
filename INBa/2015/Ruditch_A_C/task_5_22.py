#Задача 5. Вариант 22
#Напишите программу, которая бы при запуске случайным образом отображала имя одного из двух сооснователей компании Google.

#Rudich A.C.
#28.03.2016
print("Программа выводит на экран имя одного из двух сооснователей компании Google.")
import random
a = random.choice(['Сергей', 'Ларри'])
print (a)
input("\nНажмите Enter для выхода")