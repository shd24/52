epsilon = float(input('Введите точность (e):'))

sum_series = 0.0
n = 1 # Начально значение n
while True:
    t = 1 / (n**2) #Вычисляем n-ый член ряда
    if abs(t) < epsilon: #Проверяем условие остановки
        break
    sum_series += t #Добавляем член ряда к сумме
    n += 1
print ('Приблизительная сумма ряда' , sum_series)