n = int(input())
m = n % 1440
a = m // 60
b = m % 60
print(a, ' ', sep='', end='')
print(b)
