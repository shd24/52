def count_ones():
    number = input("Введите натуральное число (0 для завершения ввода): ")
    if not number.isdigit() or int(number) < 0:
        print("Ошибка: введите натуральное число (или 0 для завершения ввода).")
        return count_ones()
    number = int(number)
    if number == 0:
        return 0
    count = count_ones()
    if number == 1:
        count += 1
    return count
total_ones = count_ones()
print(f"Число 1 встречается в последовательности {total_ones} раз.")