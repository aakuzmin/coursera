#Дано четырехзначное число. Определите, является ли его десятичная запись симметричной. Если число симметричное, то выведите 1, иначе выведите любое другое целое число. Число может иметь меньше четырех знаков, тогда нужно считать, что его десятичная запись дополняется слева нулями.
#Формат ввода
#Вводится единственное число.
#Формат вывода
#Выведите ответ на задачу.
#Примечание
#Десятичная запись числа симметрична, если при прочтении слева направо и справа налево получается одно и то же число.

x = int(input())
x1 = x // 1000
x2 = x // 100 % 10
x3 = x // 10 % 10
x4 = x % 10
print((x1 * 10 + x2) - (x4 * 10 + x3) + 1)
