text = input("Введите текст: ")
consonants = "бвгджзйклмнпрстфхцчшщ"
words = text.split()
count = 0
for word in words:
     cleaned_word = ''
     for char in word:
        if char.isalpha():
            cleaned_word += char.lower()
     has_double = False
     for i in range(len(cleaned_word) - 1):
         if cleaned_word[i] in consonants and cleaned_word[i] == cleaned_word[i + 1]:
               has_double = True
               break
     if has_double:
         count += 1
print("Количество слов с удвоенной согласной:", count)