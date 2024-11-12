n = int(input("Введите количество элементов в списке: "))
my_list = []
for i in range(n):
    num = float(input(f"Введите элемент {i+1}: "))
    my_list.append(num)
max_abs_index = my_list.index(max(abs(x) for x in my_list))
min_abs_index = my_list.index(min(abs(x) for x in my_list))
if max_abs_index < min_abs_index:
    product = 1
    for i in my_list[max_abs_index + 1:min_abs_index]:
        product *= i
else:
    print("Максимальный и минимальный элементы по модулю не являются соседними.")
sorted_my_list = sorted(my_list, reverse=True)
print("Произведение элементов между максимальным и минимальным элементами по модулю:", product)
print("Отсортированный список по убыванию:")
for num in sorted_my_list:
    print(num, end=" ")