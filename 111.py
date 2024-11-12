text = input("Введите текст:")
words = text.split()
count = 0
for word in words:
    for letter in word:
        if letter.isalpha():
            if word.count(letter) > 1:
                count += 1
                break
print('Количество слов с удвоенными согласными:', count)