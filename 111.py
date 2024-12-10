def PowerA3(A):
    B = A ** 3
    return B
def is_valid_input(value):
    try:
        num = float(value)
        return True if num >= 0 else False
    except ValueError:
        return False
n = []
print("Введите 5 положительных чисел для вычисления их кубов:")
while len(n) < 5:
    user_input = input(f"Введите число {len(n) + 1}: ")
    if is_valid_input(user_input):
        n.append(float(user_input))
    else:
        print("Ошибка ввода! Пожалуйста, введите положительное вещественное число.")
c = []
for number in n:
    cube = PowerA3(number)
    c.append(cube)
print("Кубы введенных чисел:")
for i in range(5):
    print(f"{n[i]} в кубе равно {c[i]}")