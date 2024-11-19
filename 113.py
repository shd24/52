d = input("Введите элементы списка через пробел: ")
elements = d.split()
elements = [int(x) for x in elements]
max_index = -1
min_index = -1
for i in range(len(elements)):
    if max_index == -1 or abs(elements[i]) > abs(elements[max_index]):
        max_index = i
    if min_index == -1 or abs(elements[i]) < abs(elements[min_index]):
        min_index = i
startindex = min(max_index, min_index) + 1
endindex = max(max_index, min_index)
product = 1
if startindex < endindex:
    for i in range(startindex, endindex):
       product *= elements[i]
else:
    product = 0
for i in range(len(elements)):
     for j in range(0, len(elements) - i - 1):
        if elements[j] < elements[j + 1]:
            elements[j], elements[j + 1] = elements[j + 1], elements[j]
print("Произведение элементов между максимальным и минимальным по модулю:", product)
print("Упорядоченный список по убыванию:", elements)