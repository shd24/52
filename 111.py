import math
n = int(input())
if n <= 0:
    print('Число должно быть больше нуля')
else:
    c = 0
    f = 0
    while n > 0:
        t = n % 10
        f += t
        c += 1
        n //= 10
    print('Количество цифр' , c )
    print('Сумма цифр', f)