#Дано число N. С начала суток прошло N минут. Определите, сколько часов и минут будут показывать электронные часы в этот момент.
#Формат ввода
#Вводится число N — целое, положительное, не превышает 10⁷.
#Формат вывода
#Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
#Учтите, что число N может быть больше, чем количество минут в сутках.

n = int(input())
m = n % 1440
a = m // 60
b = m % 60
print(a, ' ', sep='', end='')
print(b)
