#Напишите программу, которая приветствует пользователя, выводя слово Hello, введенное имя и знаки препинания по образцу (см. пример входных и выходных данных). Программа должна считывать в строковую переменную значение и писать соответствующее приветствие. Обратите внимание, что после запятой должен обязательно стоять пробел, а перед восклицательным знаком пробела нет. Операцией конкатенации строк (+) пользоваться нельзя.
#Формат ввода
#Вводится строка, длина которой не превышает 100 символов.
#Формат вывода
#Выведите ответ на задачу.

name = input()
print('Hello, ', name, '!', sep='')
