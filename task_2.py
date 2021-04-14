# задание №2
# Пользователь вводит время в секундах. Переведите время в часы,
# минуты, секунды и выведите в формате чч:мм:сс. Используйте
# форматирование строк.

seconds = int(input('Введите количество необходимых секунд: '))
hour = seconds // 3600
minutes = (seconds - hour*3600) // 60
remains_seconds = seconds - hour*3600 - minutes*60
print(f'Вам понадобиться {hour}:{minutes}:{remains_seconds}')
