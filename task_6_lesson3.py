# Задание №6
# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
# возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(word):
    word = word.lower()
    symbols = list(word)
    symbols[0] = symbols[0].upper()
    word = ''.join(symbols)
    return word


print(int_func(input('Введите слово: ')))


