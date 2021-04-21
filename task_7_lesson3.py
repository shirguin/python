# Задание №7
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых
# пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод
# исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте
# написанную ранее функцию int_func().

def int_func(word):
    word = word.lower()
    symbols = list(word)
    symbols[0] = symbols[0].upper()
    word = ''.join(symbols)
    return word


str_words = input('Введите строку слов разделенных пробелом: ')
list_words = str_words.split(' ')
list_words_1 = []
for el in list_words:
    list_words_1.append(int_func(el))
str_words = ' '.join(list_words_1)
print(str_words)
