input_string = input('Введите строку:')
first_space_index = input_string.find(' ')
if first_space_index != -1:
    second_space_index = input_string.find(' ', first_space_index + 1)
    if second_space_index != -1:
        substring = input_string[first_space_index + 1:second_space_index]
        print("Подстрока между первым и вторым пробелом:", substring)
    else:
        print("")
else:
    print("Ошибка: строка не содержит пробела")