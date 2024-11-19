text = input("Введите строку (с пробелами): ")
f = text.find(' ')
s = text.find(' ', f + 1)
if s != -1:
   substring = text[f + 1:s]
else:
   substring = ''
print("Подстрока между первым и вторым пробелом:", substring)