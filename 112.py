while True:
    while True:
        try: epsilon = float(input('Введите точность (e):'))
        except ValueError:
            print('Введены некорректные данные')
        else: break
    if epsilon <= 0:
        print('Введено некорретное число')
    else: break
sum_series = 0
n = 1
while True:
    t = 1 / (n**2)
    if abs(t) < epsilon:
        break
    sum_series += t
    n += 1
print ('Приблизительная сумма ряда' , sum_series)