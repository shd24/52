import math
n = int(input())
if n <= 0:
    print('Число должно быть больше нуля')
else:
    c = 0
    sum_digits = 0
    while n > 0:
        digit = n % 10 #Получаем последнюю цифру
        sum_digits += digit #Добавляем цифру к сумме
        c += 1 #Увеличиваем счетчик цифр
        n //= 10 #Удаляем последнюю цифру