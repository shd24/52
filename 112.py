def IncTime(H, M, S, T):
    S += T
    M += S // 60
    S = S % 60
    H += M // 60
    M = M % 60
    H = H % 24
    return H, M, S
def get_input(p):
    while True:
        try:
            value = int(input(p))
            if value < 0:
                raise ValueError("Значение должно быть положительным.")
            return value
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Пожалуйста, попробуйте еще раз.")
H = get_input("Введите часы (0-23): ")
M = get_input("Введите минуты (0-59): ")
S = get_input("Введите секунды (0-59): ")
T = get_input("Введите количество секунд для увеличения времени: ")
new_H, new_M, new_S = IncTime(H, M, S, T)
print(f"Новое время: {new_H} часов, {new_M} минут, {new_S} секунд")